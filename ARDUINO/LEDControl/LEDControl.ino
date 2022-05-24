#include <ArduinoSerial.h>
#include <RomiSerial.h>
#include <RomiSerialErrors.h>
#include <stdint.h>
#include "clock.h"
#include "PeriodicActivity.h"
#include "ActivityManager.h"

using namespace romiserial;

extern volatile int32_t current_time_ms;
extern volatile uint8_t current_interrupt;

void send_info(RomiSerial *romiSerial, int16_t *args, const char *string_arg);
void handle_add_analogue_measure(RomiSerial *romiSerial, int16_t *args, const char *string_arg);
void handle_add_digital_pulse(RomiSerial *romiSerial, int16_t *args, const char *string_arg);
void handle_add_master_digital_pulse(RomiSerial *romiSerial, int16_t *args, const char *string_arg);

void handle_stop_measurements(RomiSerial *romiSerial, int16_t *args, const char *string_arg);
void handle_start_mesurements(RomiSerial *romiSerial, int16_t *args, const char *string_arg);
void handle_reset(RomiSerial *romiSerial, int16_t *args, const char *string_arg);

const static MessageHandler handlers[] = {
        { 'a', 5, false, handle_add_analogue_measure },
        { 'd', 9, false, handle_add_digital_pulse },
        { 'm', 9, false, handle_add_master_digital_pulse },
        { 'b', 0, false, handle_start_mesurements },
        { 'e', 0, false, handle_stop_measurements },
        { 'r', 0, false, handle_reset },
        { '?', 0, false, send_info },
};

//RomiSerial romiSerial(get_default_input(), get_default_output(), handlers, sizeof(handlers) / sizeof(MessageHandler));
RomiSerial *romiSerial;
ArduinoSerial serial(Serial);
ActivityManager activityManager;

const int RelayPin = 8;

void setup()
{
  Serial.begin(115200);
  while (!Serial)
    ;
  // Serial port now setup when get_default_functions_called.
  romiSerial = new RomiSerial(serial, serial, handlers, sizeof(handlers) / sizeof(MessageHandler));
  pinMode(RelayPin, OUTPUT);
  digitalWrite(RelayPin, LOW);

}

void loop()
{
        romiSerial->handle_input();
        //Serial.println(current_time_ms);
        delay(1000);
}

void send_info(RomiSerial *romiSerial, int16_t *args, const char *string_arg)
{
        romiSerial->send("[\"PAMFluo\",\"0.1\"]"); 
}

  
void handle_add_analogue_measure(RomiSerial *romiSerial, int16_t *args, const char *string_arg)
{        
    if (activityManager.AddAnalogueMeasure(args[0], args[1], args[2], args[3], args[4]))
        romiSerial->send_ok();
    else
        romiSerial->send_error(kInvalidOpcode, "max activities exceeded.");
}

void handle_add_digital_pulse(RomiSerial *romiSerial, int16_t *args, const char *string_arg)
{
    int32_t start_delay_ms = (int32_t) args[1] * 1000 + args[2];
    int32_t duration = (int32_t) args[3] * 1000 + args[4];
    int32_t period = (int32_t) args[5] * 1000 + args[6];
    if (activityManager.AddDigitalPulse(args[0], start_delay_ms, duration, period, args[7], args[8]))
            romiSerial->send_ok();
    else
        romiSerial->send_error(kInvalidOpcode, "max activities exceeded.");
}

void handle_add_master_digital_pulse(RomiSerial *romiSerial, int16_t *args, const char *string_arg)
{
    int32_t start_delay_ms = (int32_t) args[1] * 1000 + args[2];
    int32_t duration = (int32_t) args[3] * 1000 + args[4];
    int32_t period = (int32_t) args[5] * 1000 + args[6];
    if (activityManager.AddMasterDigitalPulse(args[0], start_delay_ms, duration, period, args[7], args[8]))            
            romiSerial->send_ok();
   
    else
        romiSerial->send_error(kInvalidOpcode, "max activities exceeded.");
}

void handle_stop_measurements(RomiSerial *romiSerial, int16_t *args, const char *string_arg)
{
        activityManager.enable(false);
        romiSerial->send_ok();
}

void handle_start_mesurements(RomiSerial *romiSerial, int16_t *args, const char *string_arg)
{
        clock_register_activities(activityManager.Activities(), activityManager.NumberActivities());

        // Initialize the interrupt timer.
        cli();
        clock_init();
        sei();
        // Start the interrupt timer.
        clock_run();
        digitalWrite(RelayPin, HIGH);

        activityManager.enable(true);
        romiSerial->send_ok();
}

void handle_reset(RomiSerial *romiSerial, int16_t *args, const char *string_arg)
{
        digitalWrite(RelayPin, LOW);
        romiSerial->send_ok();

}
