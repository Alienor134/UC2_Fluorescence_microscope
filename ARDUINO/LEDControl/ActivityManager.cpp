

#include "Arduino.h"
#include "ActivityManager.h"

ActivityManager::ActivityManager() : current_number_activities(0)
{
    for (uint8_t index = 0; index < MAX_ACTIVITIES; index++)
    {
        activities[index] = nullptr;
    }
}

ActivityManager::~ActivityManager()
{
    for (uint8_t index = 0; index < current_number_activities; index++)
    {
        delete activities[index];
        activities[index] = nullptr;
    }
}

bool ActivityManager::AddActivity(PeriodicActivity *newactivity)
{
    bool retval = false;
    if (newactivity != nullptr)
    {
        activities[current_number_activities++] = newactivity;
        retval = true;
    }
    return retval;
}


bool ActivityManager::AddDigitalPulse(int32_t pin, int32_t start_delay_ms, int32_t duration, int32_t period, int32_t slave, int32_t analog_value)
{
    bool retval = false;

    if (current_number_activities < MAX_ACTIVITIES)
    {
        auto newactivity = new DigitalPulse(pin, start_delay_ms, duration, period, slave, analog_value);
        retval = AddActivity(newactivity);
    }
    return retval;
}

bool ActivityManager::AddMasterDigitalPulse(int32_t pin, int32_t start_delay_ms, int32_t duration, int32_t period, int32_t slave, int32_t analog_value)
{
    bool retval = false;
    int8_t current_number_slaves = 0;
    if (current_number_activities < MAX_ACTIVITIES)
    {
        auto newactivity = new MasterDigitalPulse(pin, start_delay_ms, duration, period, slave, analog_value);
        retval = AddActivity(newactivity);
        for (int i = 0; i < current_number_activities;  i++)
        {
            if(activities[i]->is_slave()>0)
            {
                newactivity->AddSlave(activities[i]);
            }
        }        
    }
    return retval;
}

bool ActivityManager::AddAnalogueMeasure(int32_t pin, int32_t start_delay_ms, int32_t duration, int32_t period, int32_t slave)
{
        bool retval = false;
        if (current_number_activities < MAX_ACTIVITIES)
        {
            auto newactivity = new AnalogMeasure(pin, start_delay_ms, duration, period, slave);
            retval = AddActivity(newactivity);
        }
        return retval;
}

PeriodicActivity **ActivityManager::Activities()
{
    return activities;
}

uint8_t ActivityManager::NumberActivities()
{
    return current_number_activities;
}

void ActivityManager::enable(bool enabled)
{
    for (uint8_t index = 0; index < current_number_activities; index++)
    {
        if (enabled)
            activities[index]->enable();
        else
            activities[index]->disable();
    }
}
