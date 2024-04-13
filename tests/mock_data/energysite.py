ENERGYSITE_SOLAR = {
    "energy_site_id": 12345,
    "resource_type": "solar",
    "id": "313dbc37-555c-45b1-83aa-62a4ef9ff7ac",
    "asset_site_id": "12345",
    "solar_power": 2260,
    "solar_type": "pv_panel",
    "storm_mode_enabled": None,
    "powerwall_onboarding_settings_set": None,
    "sync_grid_alert_enabled": False,
    "breaker_alert_enabled": False,
    "components": {
        "battery": False,
        "solar": True,
        "solar_type": "pv_panel",
        "grid": True,
        "load_meter": True,
        "market_type": "residential",
    },
}

ENERGYSITE_BATTERY = {
    "energy_site_id": 67890,
    "resource_type": "battery",
    "site_name": "Battery Home",
    "id": "XXX",
    "asset_site_id": "67890",
    "solar_power": 3456,
    "solar_type": "pv_panel",
    "storm_mode_enabled": None,
    "powerwall_onboarding_settings_set": None,
    "sync_grid_alert_enabled": False,
    "breaker_alert_enabled": False,
    "components": {
        "battery": True,
        "solar": True,
        "solar_type": "pv_panel",
        "grid": True,
        "load_meter": True,
        "market_type": "residential",
    },
}

SITE_CONFIG_SOLAR = {
    "id": "313dbc37-555c-45b1-83aa-62a4ef9ff7ac",
    "site_name": "My Home",
    "site_number": "2252147638651575",
    "installation_date": "2022-04-04T15:56:35-07:00",
    "user_settings": {
        "storm_mode_enabled": None,
        "powerwall_onboarding_settings_set": None,
        "sync_grid_alert_enabled": False,
        "breaker_alert_enabled": False,
    },
    "components": {
        "solar": True,
        "solar_type": "pv_panel",
        "battery": False,
        "grid": True,
        "backup": False,
        "gateway": "gateway_type_none",
        "load_meter": True,
        "tou_capable": False,
        "storm_mode_capable": False,
        "flex_energy_request_capable": False,
        "car_charging_data_supported": False,
        "off_grid_vehicle_charging_reserve_supported": False,
        "vehicle_charging_performance_view_enabled": False,
        "vehicle_charging_solar_offset_view_enabled": False,
        "battery_solar_offset_view_enabled": False,
        "energy_service_self_scheduling_enabled": True,
        "rate_plan_manager_supported": True,
        "configurable": False,
        "grid_services_enabled": False,
    },
    "installation_time_zone": "America/Los_Angeles",
    "time_zone_offset": -420,
    "geolocation": {"latitude": 32.53452700000001, "longitude": -112.3463137},
    "address": {
        "address_line1": "1234 Tesla Solar Ave",
        "city": "Austin",
        "state": "TX",
        "zip": "123456",
        "country": "US",
    },
}

SITE_CONFIG_POWERWALL = {
    "id": "XXX",
    "site_name": "Battery Home",
    "backup_reserve_percent": 0,
    "default_real_mode": "self_consumption",
    "installation_date": "2022-03-21T17:15:23+10:00",
    "user_settings": {
        "storm_mode_enabled": True,
        "powerwall_onboarding_settings_set": True,
        "sync_grid_alert_enabled": True,
        "breaker_alert_enabled": False,
    },
    "components": {
        "solar": True,
        "solar_type": "pv_panel",
        "battery": True,
        "grid": True,
        "backup": True,
        "gateway": "teg",
        "load_meter": True,
        "tou_capable": True,
        "storm_mode_capable": True,
        "flex_energy_request_capable": False,
        "car_charging_data_supported": False,
        "off_grid_vehicle_charging_reserve_supported": False,
        "vehicle_charging_performance_view_enabled": False,
        "vehicle_charging_solar_offset_view_enabled": False,
        "battery_solar_offset_view_enabled": True,
        "solar_value_enabled": True,
        "energy_value_header": "Energy Value",
        "energy_value_subheader": "Estimated Value",
        "energy_service_self_scheduling_enabled": True,
        "show_grid_import_battery_source_cards": True,
        "set_islanding_mode_enabled": True,
        "wifi_commissioning_enabled": True,
        "backup_time_remaining_enabled": True,
        "rate_plan_manager_supported": True,
        "battery_type": "ac_powerwall",
        "configurable": True,
        "grid_services_enabled": False,
        "customer_preferred_export_rule": "battery_ok",
        "net_meter_mode": "battery_ok",
        "edit_setting_permission_to_export": True,
        "edit_setting_grid_charging": True,
        "edit_setting_energy_exports": True,
    },
    "version": "22.18.3 21c0ad81",
    "battery_count": 1,
    "tariff_content": {
        "name": "Wholesale",
        "utility": "Amber",
        "daily_charges": [{"amount": 0, "name": "Charge"}],
        "demand_charges": {"ALL": {"ALL": 0}, "Summer": {}, "Winter": {}},
        "energy_charges": {
            "ALL": {"ALL": 0},
            "Summer": {"ON_PEAK": 0.44, "PARTIAL_PEAK": 0.3},
            "Winter": {},
        },
        "seasons": {
            "Summer": {
                "fromDay": 1,
                "toDay": 31,
                "fromMonth": 1,
                "toMonth": 12,
                "tou_periods": {
                    "ON_PEAK": [
                        {
                            "fromDayOfWeek": 0,
                            "toDayOfWeek": 6,
                            "fromHour": 3,
                            "fromMinute": 0,
                            "toHour": 5,
                            "toMinute": 0,
                        },
                        {
                            "fromDayOfWeek": 0,
                            "toDayOfWeek": 6,
                            "fromHour": 6,
                            "fromMinute": 0,
                            "toHour": 7,
                            "toMinute": 30,
                        },
                        {
                            "fromDayOfWeek": 0,
                            "toDayOfWeek": 6,
                            "fromHour": 16,
                            "fromMinute": 0,
                            "toHour": 21,
                            "toMinute": 0,
                        },
                        {
                            "fromDayOfWeek": 0,
                            "toDayOfWeek": 6,
                            "fromHour": 23,
                            "fromMinute": 0,
                            "toHour": 1,
                            "toMinute": 0,
                        },
                    ],
                    "PARTIAL_PEAK": [
                        {
                            "fromDayOfWeek": 0,
                            "toDayOfWeek": 6,
                            "fromHour": 7,
                            "fromMinute": 30,
                            "toHour": 10,
                            "toMinute": 30,
                        },
                        {
                            "fromDayOfWeek": 0,
                            "toDayOfWeek": 6,
                            "fromHour": 14,
                            "fromMinute": 0,
                            "toHour": 16,
                            "toMinute": 0,
                        },
                    ],
                    "OFF_PEAK": [
                        {
                            "fromDayOfWeek": 0,
                            "toDayOfWeek": 6,
                            "fromHour": 1,
                            "fromMinute": 0,
                            "toHour": 3,
                            "toMinute": 0,
                        },
                        {
                            "fromDayOfWeek": 0,
                            "toDayOfWeek": 6,
                            "fromHour": 5,
                            "fromMinute": 0,
                            "toHour": 6,
                            "toMinute": 0,
                        },
                        {
                            "fromDayOfWeek": 0,
                            "toDayOfWeek": 6,
                            "fromHour": 10,
                            "fromMinute": 30,
                            "toHour": 14,
                            "toMinute": 0,
                        },
                        {
                            "fromDayOfWeek": 0,
                            "toDayOfWeek": 6,
                            "fromHour": 21,
                            "fromMinute": 0,
                            "toHour": 23,
                            "toMinute": 0,
                        },
                    ],
                },
            },
            "Winter": {
                "fromDay": 0,
                "toDay": 0,
                "fromMonth": 0,
                "toMonth": 0,
                "tou_periods": {},
            },
        },
        "sell_tariff": {
            "name": "Wholesale",
            "utility": "Amber",
            "daily_charges": [{"amount": 0, "name": "Charge"}],
            "demand_charges": {"ALL": {"ALL": 0}, "Summer": {}, "Winter": {}},
            "energy_charges": {
                "ALL": {"ALL": 0},
                "Summer": {"ON_PEAK": 0.32, "PARTIAL_PEAK": 0.04},
                "Winter": {},
            },
            "seasons": {
                "Summer": {
                    "fromDay": 1,
                    "toDay": 31,
                    "fromMonth": 1,
                    "toMonth": 12,
                    "tou_periods": {
                        "ON_PEAK": [
                            {
                                "fromDayOfWeek": 0,
                                "toDayOfWeek": 6,
                                "fromHour": 3,
                                "fromMinute": 0,
                                "toHour": 5,
                                "toMinute": 0,
                            },
                            {
                                "fromDayOfWeek": 0,
                                "toDayOfWeek": 6,
                                "fromHour": 6,
                                "fromMinute": 0,
                                "toHour": 7,
                                "toMinute": 30,
                            },
                            {
                                "fromDayOfWeek": 0,
                                "toDayOfWeek": 6,
                                "fromHour": 16,
                                "fromMinute": 0,
                                "toHour": 21,
                                "toMinute": 0,
                            },
                            {
                                "fromDayOfWeek": 0,
                                "toDayOfWeek": 6,
                                "fromHour": 23,
                                "fromMinute": 0,
                                "toHour": 1,
                                "toMinute": 0,
                            },
                        ],
                        "PARTIAL_PEAK": [
                            {
                                "fromDayOfWeek": 0,
                                "toDayOfWeek": 6,
                                "fromHour": 7,
                                "fromMinute": 30,
                                "toHour": 10,
                                "toMinute": 30,
                            },
                            {
                                "fromDayOfWeek": 0,
                                "toDayOfWeek": 6,
                                "fromHour": 14,
                                "fromMinute": 0,
                                "toHour": 16,
                                "toMinute": 0,
                            },
                        ],
                        "OFF_PEAK": [
                            {
                                "fromDayOfWeek": 0,
                                "toDayOfWeek": 6,
                                "fromHour": 1,
                                "fromMinute": 0,
                                "toHour": 3,
                                "toMinute": 0,
                            },
                            {
                                "fromDayOfWeek": 0,
                                "toDayOfWeek": 6,
                                "fromHour": 5,
                                "fromMinute": 0,
                                "toHour": 6,
                                "toMinute": 0,
                            },
                            {
                                "fromDayOfWeek": 0,
                                "toDayOfWeek": 6,
                                "fromHour": 10,
                                "fromMinute": 30,
                                "toHour": 14,
                                "toMinute": 0,
                            },
                            {
                                "fromDayOfWeek": 0,
                                "toDayOfWeek": 6,
                                "fromHour": 21,
                                "fromMinute": 0,
                                "toHour": 23,
                                "toMinute": 0,
                            },
                        ],
                    },
                },
                "Winter": {
                    "fromDay": 0,
                    "toDay": 0,
                    "fromMonth": 0,
                    "toMonth": 0,
                    "tou_periods": {},
                },
            },
        },
    },
    "nameplate_power": 5000,
    "nameplate_energy": 13500,
    "installation_time_zone": "Australia/Brisbane",
    "max_site_meter_power_ac": 1000000000,
    "min_site_meter_power_ac": -1000000000,
    "geolocation": {"latitude": -123.456, "longitude": 123.456},
    "address": {
        "address_line1": "XXX",
        "city": "YYYY",
        "state": "QLD",
        "zip": "NNN",
        "country": "AU",
    },
}

SITE_DATA = {
    "solar_power": 7720,
    "total_pack_energy": 1,
    "percentage_charged": 0,
    "battery_power": 0,
    "load_power": 4517.14990234375,
    "grid_status": "Unknown",
    "grid_services_active": False,
    "grid_power": -3202.85009765625,
    "grid_services_power": 0,
    "generator_power": 0,
    "island_status": "island_status_unknown",
    "storm_mode_active": False,
    "timestamp": "2022-07-28T17:11:27Z",
    "wall_connectors": None,
}

BATTERY_DATA = {
    "site_name": "Battery Home",
    "total_pack_energy": 1,
    "grid_status": "Active",
    "backup": {
        "backup_reserve_percent": 0,
        "events": [
            {"timestamp": "2022-07-12T06:56:55+10:00", "duration": 38773},
            {"timestamp": "2022-07-11T20:46:25+10:00", "duration": 66479},
            {"timestamp": "2022-06-29T11:35:43+10:00", "duration": 842030},
            {"timestamp": "2022-06-18T15:28:35+10:00", "duration": 1013486},
            {"timestamp": "2022-06-15T15:43:20+10:00", "duration": 210737},
            {"timestamp": "2022-06-10T08:26:12+10:00", "duration": 47649},
            {"timestamp": "2022-06-03T13:58:52+10:00", "duration": 443079},
            {"timestamp": "2022-05-15T10:46:58+10:00", "duration": 31389950},
            {"timestamp": "2022-05-14T15:33:38+10:00", "duration": 1279604},
            {"timestamp": "2022-05-07T19:39:07+10:00", "duration": 901817},
            {"timestamp": "2022-04-23T08:26:14+10:00", "duration": 437693},
            {"timestamp": "2022-04-22T19:14:33+10:00", "duration": 757615},
            {"timestamp": "2022-04-14T11:54:35+10:00", "duration": 581358},
            {"timestamp": "2022-04-06T22:26:41+10:00", "duration": 65188},
            {"timestamp": "2022-04-03T22:12:07+10:00", "duration": 654161},
            {"timestamp": "2022-04-03T21:57:36+10:00", "duration": 798912},
            {"timestamp": "2022-04-03T18:51:05+10:00", "duration": 67764},
            {"timestamp": "2022-04-03T17:22:58+10:00", "duration": 641782},
            {"timestamp": "2022-04-03T17:21:19+10:00", "duration": 69942},
            {"timestamp": "2022-04-03T06:34:17+10:00", "duration": 232350},
            {"timestamp": "2022-04-02T19:05:41+10:00", "duration": 47104},
            {"timestamp": "2022-04-02T09:35:18+10:00", "duration": 258895},
            {"timestamp": "2022-04-02T05:21:14+10:00", "duration": 63814},
            {"timestamp": "2022-04-01T11:59:57+10:00", "duration": 586849},
            {"timestamp": "2022-04-01T11:50:56+10:00", "duration": 457199},
            {"timestamp": "2022-04-01T11:48:21+10:00", "duration": 51065},
            {"timestamp": "2022-04-01T11:47:23+10:00", "duration": 41783},
            {"timestamp": "2022-04-01T11:01:46+10:00", "duration": 73278},
            {"timestamp": "2022-03-31T17:12:00+10:00", "duration": 45838},
            {"timestamp": "2022-03-24T16:28:07+10:00", "duration": 122233},
            {"timestamp": "2022-03-24T06:15:44+10:00", "duration": 5932791},
            {"timestamp": "2022-03-23T17:01:37+10:00", "duration": 210322},
            {"timestamp": "2022-03-23T16:11:27+10:00", "duration": 2608373},
            {"timestamp": "2022-03-21T21:04:54+10:00", "duration": 296080},
        ],
        "events_count": 0,
        "total_events": 0,
    },
    "user_settings": {
        "storm_mode_enabled": True,
        "powerwall_onboarding_settings_set": True,
        "sync_grid_alert_enabled": False,
        "breaker_alert_enabled": False,
    },
    "components": {
        "solar": True,
        "solar_type": "pv_panel",
        "battery": True,
        "grid": True,
        "backup": True,
        "gateway": "teg",
        "load_meter": True,
        "tou_capable": True,
        "storm_mode_capable": True,
        "flex_energy_request_capable": False,
        "car_charging_data_supported": False,
        "off_grid_vehicle_charging_reserve_supported": False,
        "vehicle_charging_performance_view_enabled": False,
        "vehicle_charging_solar_offset_view_enabled": False,
        "battery_solar_offset_view_enabled": True,
        "solar_value_enabled": True,
        "energy_value_header": "Energy Value",
        "energy_value_subheader": "Estimated Value",
        "show_grid_import_battery_source_cards": True,
        "backup_time_remaining_enabled": True,
        "rate_plan_manager_supported": True,
        "battery_type": "ac_powerwall",
        "configurable": False,
        "grid_services_enabled": False,
        "customer_preferred_export_rule": "battery_ok",
        "net_meter_mode": "battery_ok",
    },
    "default_real_mode": "self_consumption",
    "operation": "self_consumption",
    "installation_date": "2022-03-21T17:15:23+10:00",
    "load_power": 7010,
    "solar_power": 6638,
    "grid_power": 2,
    "battery_power": 370,
    "generator_power": 0,
    "power_reading": [
        {
            "timestamp": "2022-08-18T15:10:20+10:00",
            "load_power": 7010,
            "solar_power": 6638,
            "grid_power": 2,
            "battery_power": 370,
            "generator_power": 0,
        }
    ],
    "battery_count": 0,
}

BATTERY_SUMMARY = {
    "site_name": "Battery Home",
    "id": "XXX",
    "total_pack_energy": 14056,
    "percentage_charged": 96.8322199922116,
    "battery_power": 370,
    "grid_status": "Active",
}
