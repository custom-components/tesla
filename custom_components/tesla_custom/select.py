"""Support for Tesla selects."""
import logging

from teslajsonpy.car import TeslaCar

from homeassistant.components.select import SelectEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import EntityCategory

from . import TeslaDataUpdateCoordinator
from .base import TeslaCarDevice
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

HEATER_OPTIONS = [
    "Off",
    "Low",
    "Medium",
    "High",
]

CABIN_OPTIONS = [
    "Off",
    "No A/C",
    "On",
]

SEAT_ID_MAP = {
    "left": 0,
    "right": 1,
    "rear_left": 2,
    "rear_center": 4,
    "rear_right": 5,
    "third_row_left": 6,
    "third_row_right": 7,
}


async def async_setup_entry(hass: HomeAssistant, config_entry, async_add_entities):
    """Set up the Tesla selects by config_entry."""
    coordinator = hass.data[DOMAIN][config_entry.entry_id]["coordinator"]
    entities = []
    for car in coordinator.controller.cars.values():
        entities.append(TeslaCabinOverheatProtection(hass, car, coordinator))
        for seat_name in SEAT_ID_MAP:
            if "rear" in seat_name and not car.rear_heated_seats:
                continue
            if "third_row" in seat_name and not car.third_row_seats:
                continue
            entities.append(HeatedSeatSelect(hass, car, coordinator, seat_name))

    async_add_entities(entities, True)


class HeatedSeatSelect(TeslaCarDevice, SelectEntity):
    """Representation of a Tesla Heated Seat Select."""

    def __init__(
        self,
        hass: HomeAssistant,
        car: TeslaCar,
        coordinator: TeslaDataUpdateCoordinator,
        seat_name: str,
    ):
        """Initialize a heated seat for the vehicle."""
        super().__init__(hass, car, coordinator)

        self._seat_name = seat_name
        self.type = f"heated seat {seat_name}"

    async def async_select_option(self, option: str, **kwargs):
        """Change the selected option."""
        level: int = HEATER_OPTIONS.index(option)

        # await wait_for_climate(self.hass, self.config_entry_id)
        _LOGGER.debug("Setting %s to %s", self.name, level)
        await self._car.remote_seat_heater_request(level, SEAT_ID_MAP[self._seat_name])

        await self.update_controller(force=True)

    @property
    def current_option(self):
        """Return the selected entity option to represent the entity state."""
        current_value = self._car.get_seat_heater_status(SEAT_ID_MAP[self._seat_name])

        if current_value is None:
            return HEATER_OPTIONS[0]
        return HEATER_OPTIONS[current_value]

    @property
    def _seat_key(self):
        return f"seat_heater_{self._seat_name}"

    @property
    def options(self):
        """Return a set of selectable options."""
        return HEATER_OPTIONS


class TeslaCabinOverheatProtection(TeslaCarDevice, SelectEntity):
    """Representation of a Tesla Heated Seat Select."""

    def __init__(
        self,
        hass: HomeAssistant,
        car: TeslaCar,
        coordinator: TeslaDataUpdateCoordinator,
    ):
        """Initialize a heated seat for the vehicle."""
        super().__init__(hass, car, coordinator)

        self.type = "cabin overheat protection"
        self._attr_options = CABIN_OPTIONS
        self._attr_entity_category = EntityCategory.CONFIG

    async def async_select_option(self, option: str, **kwargs):
        """Change the selected option."""
        await self._car.set_cabin_overheat_protection(option)

    @property
    def current_option(self):
        """Return the selected entity option to represent the entity state."""
        return self._car.cabin_overheat_protection
