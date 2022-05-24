#include <avr/io.h>
#include <avr/interrupt.h>
#include "PeriodicActivity.h"

#ifndef _CLOCK_H_
#define _CLOCK_H_

void clock_init();

void clock_register_activities(PeriodicActivity **activities, int num_activities);

#define clock_run()                                          \
        {                                                               \
                /* Initialize counter */                                \
                TCNT1 = 0;                                              \
                /* Enable Timer1 */                                     \
                TIMSK1 |= (1 << OCIE1A);                                \
        }

#define clock_pause()                                         \
        {                                                               \
                /* Disable Timer1 interrupt */                          \
                TIMSK1 &= ~(1 << OCIE1A);                               \
        }

#endif // _CLOCK_H_
