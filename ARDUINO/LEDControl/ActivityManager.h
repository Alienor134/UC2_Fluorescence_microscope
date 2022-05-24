//
// Created by douglas on 12/02/2021.
//

#ifndef ROMI_ROVER_BUILD_AND_TEST_ACTIVITYMANAGER_H
#define ROMI_ROVER_BUILD_AND_TEST_ACTIVITYMANAGER_H

#include "PeriodicActivity.h"

#define MAX_ACTIVITIES 10

class ActivityManager
{
public:
    explicit ActivityManager();
    virtual ~ActivityManager();
    bool AddDigitalPulse(int32_t pin, int32_t start_delay_ms, int32_t duration, int32_t period, int32_t slave, int32_t analog_value);
    bool AddMasterDigitalPulse(int32_t pin, int32_t start_delay_ms, int32_t duration, int32_t period, int32_t slave, int32_t analog_value);
    bool AddAnalogueMeasure(int32_t pin, int32_t start_delay_ms, int32_t duration, int32_t period, int32_t slave);
    PeriodicActivity **Activities();

    uint8_t NumberActivities();

    void enable(bool enabled);
private:
    bool AddActivity(PeriodicActivity *activity);
private:
    PeriodicActivity *activities[MAX_ACTIVITIES];
    uint8_t current_number_activities;

};



#endif //ROMI_ROVER_BUILD_AND_TEST_ACTIVITYMANAGER_H
