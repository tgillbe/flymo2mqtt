from .packet import Request, Response, Parameter

class ChallengeResponseV2Response(Response):
    authentication_successful: bool

    def __init__(self, authentication_successful: bool = False):
        self.authentication_successful = authentication_successful
        super().__init__(
            4664,
            11,
            [
                Parameter("authentication_successful", "bool"),
            ])

class EnterOperatorPinResponse(Response):
    def __init__(self):
        super().__init__(
            4664,
            4)

class GetBlockedTimeResponse(Response):
    blocked_time: int

    def __init__(self, blocked_time: int = 0):
        self.blocked_time = blocked_time
        super().__init__(
            4664,
            2,
            [
                Parameter("blocked_time", "u32"),
            ])

class GetLoginLevelResponse(Response):
    login_level: int

    def __init__(self, login_level: int = 0):
        self.login_level = login_level
        super().__init__(
            4664,
            0,
            [
                Parameter("login_level", "u8"),
            ])

class GetRemainingLoginAttemptsResponse(Response):
    operator: int
    service: int
    advanced: int

    def __init__(self, operator: int = 0, service: int = 0, advanced: int = 0):
        self.operator = operator
        self.service = service
        self.advanced = advanced
        super().__init__(
            5124,
            10,
            [
                Parameter("operator", "u32"),
                Parameter("service", "u32"),
                Parameter("advanced", "u32"),
            ])

class GetSecurityCodeV2Response(Response):
    key_id: int
    security_code: bytes

    def __init__(self, key_id: int = 0, security_code: bytes = bytes()):
        self.key_id = key_id
        self.security_code = security_code
        super().__init__(
            4664,
            14,
            [
                Parameter("key_id", "u32"),
                Parameter("security_code", "bytes"),
            ])

class InitiateAuthenticationV2Response(Response):
    key_id: int
    challenge: bytes

    def __init__(self, key_id: int = 0, challenge: bytes = bytes()):
        self.key_id = key_id
        self.challenge = challenge
        super().__init__(
            4664,
            10,
            [
                Parameter("key_id", "u32"),
                Parameter("challenge", "bytes"),
            ])

class IsBlockedResponse(Response):
    is_blocked: bool

    def __init__(self, is_blocked: bool = False):
        self.is_blocked = is_blocked
        super().__init__(
            4664,
            1,
            [
                Parameter("is_blocked", "bool"),
            ])

class IsOperatorLoggedInResponse(Response):
    operator_logged_in: bool

    def __init__(self, operator_logged_in: bool = False):
        self.operator_logged_in = operator_logged_in
        super().__init__(
            4664,
            3,
            [
                Parameter("operator_logged_in", "bool"),
            ])

class IsTrustedToEnterSafetyPinResponse(Response):
    trusted: bool

    def __init__(self, trusted: bool = False):
        self.trusted = trusted
        super().__init__(
            4664,
            8,
            [
                Parameter("trusted", "bool"),
            ])

class LogoutResponse(Response):
    def __init__(self):
        super().__init__(
            4664,
            15)

class SetOperatorPinResponse(Response):
    def __init__(self):
        super().__init__(
            4664,
            5)

class SubscribeAllEventsResponse(Response):
    def __init__(self):
        super().__init__(
            4664,
            17)

class GetAllSettingsResponse(Response):
    available: bool
    enabled: bool
    sensitivity: int

    def __init__(self, available: bool = False, enabled: bool = False, sensitivity: int = 0):
        self.available = available
        self.enabled = enabled
        self.sensitivity = sensitivity
        super().__init__(
            4460,
            8,
            [
                Parameter("available", "bool"),
                Parameter("enabled", "bool"),
                Parameter("sensitivity", "u8"),
            ])

class GetAvailableResponse(Response):
    available: bool

    def __init__(self, available: bool = False):
        self.available = available
        super().__init__(
            4460,
            2,
            [
                Parameter("available", "bool"),
            ])

class GetEnabledResponse(Response):
    enabled: bool

    def __init__(self, enabled: bool = False):
        self.enabled = enabled
        super().__init__(
            4460,
            4,
            [
                Parameter("enabled", "bool"),
            ])

class GetRestrictionReasonResponse(Response):
    restriction_reason: int

    def __init__(self, restriction_reason: int = 0):
        self.restriction_reason = restriction_reason
        super().__init__(
            4460,
            9,
            [
                Parameter("restriction_reason", "u8"),
            ])

class GetSensitivityResponse(Response):
    sensitivity: int

    def __init__(self, sensitivity: int = 0):
        self.sensitivity = sensitivity
        super().__init__(
            4460,
            6,
            [
                Parameter("sensitivity", "u8"),
            ])

class IsReadyResponse(Response):
    is_ready: bool

    def __init__(self, is_ready: bool = False):
        self.is_ready = is_ready
        super().__init__(
            4460,
            10,
            [
                Parameter("is_ready", "bool"),
            ])

class SetAvailableResponse(Response):
    def __init__(self):
        super().__init__(
            4460,
            3)

class SetEnabledResponse(Response):
    def __init__(self):
        super().__init__(
            4460,
            5)

class SetSensitivityResponse(Response):
    def __init__(self):
        super().__init__(
            4460,
            7)

class SubscribeAllEventsResponse(Response):
    def __init__(self):
        super().__init__(
            4460,
            0)

class SubscribeEventChannelResponse(Response):
    def __init__(self):
        super().__init__(
            4460,
            1)

class GetBatteryLevelResponse(Response):
    battery_level: int

    def __init__(self, battery_level: int = 0):
        self.battery_level = battery_level
        super().__init__(
            4106,
            20,
            [
                Parameter("battery_level", "u8"),
            ])

class GetCapacityResponse(Response):
    capacity: int

    def __init__(self, capacity: int = 0):
        self.capacity = capacity
        super().__init__(
            4106,
            0,
            [
                Parameter("capacity", "s16"),
            ])

class GetEnergyLevelResponse(Response):
    energy_level: int

    def __init__(self, energy_level: int = 0):
        self.energy_level = energy_level
        super().__init__(
            4106,
            1,
            [
                Parameter("energy_level", "s16"),
            ])

class GetRemainingChargingTimeResponse(Response):
    remaining_charging_time: int

    def __init__(self, remaining_charging_time: int = 0):
        self.remaining_charging_time = remaining_charging_time
        super().__init__(
            4106,
            22,
            [
                Parameter("remaining_charging_time", "u32"),
            ])

class GetSimulatedEnergyLevelResponse(Response):
    energy_level: int

    def __init__(self, energy_level: int = 0):
        self.energy_level = energy_level
        super().__init__(
            4106,
            3,
            [
                Parameter("energy_level", "s16"),
            ])

class GetSimulationResponse(Response):
    on_off: bool

    def __init__(self, on_off: bool = False):
        self.on_off = on_off
        super().__init__(
            4106,
            5,
            [
                Parameter("on_off", "bool"),
            ])

class IsChargingResponse(Response):
    is_charging: bool

    def __init__(self, is_charging: bool = False):
        self.is_charging = is_charging
        super().__init__(
            4106,
            21,
            [
                Parameter("is_charging", "bool"),
            ])

class SetSimulatedEnergyLevelResponse(Response):
    energy_level: int

    def __init__(self, energy_level: int = 0):
        self.energy_level = energy_level
        super().__init__(
            4106,
            2,
            [
                Parameter("energy_level", "s16"),
            ])

class SetSimulationResponse(Response):
    on_off: bool

    def __init__(self, on_off: bool = False):
        self.on_off = on_off
        super().__init__(
            4106,
            4,
            [
                Parameter("on_off", "bool"),
            ])

class DisablePairableResponse(Response):
    def __init__(self):
        super().__init__(
            4678,
            7)

class ErasePairedDeviceListResponse(Response):
    def __init__(self):
        super().__init__(
            4678,
            3)

class GetAdvertisingResponse(Response):
    value: bool

    def __init__(self, value: bool = False):
        self.value = value
        super().__init__(
            4678,
            9,
            [
                Parameter("value", "bool"),
            ])

class GetConnectedResponse(Response):
    value: bool

    def __init__(self, value: bool = False):
        self.value = value
        super().__init__(
            4678,
            2,
            [
                Parameter("value", "bool"),
            ])

class GetPairableResponse(Response):
    value: bool

    def __init__(self, value: bool = False):
        self.value = value
        super().__init__(
            4678,
            1,
            [
                Parameter("value", "bool"),
            ])

class SetAdvertisingResponse(Response):
    def __init__(self):
        super().__init__(
            4678,
            8)

class SetPairableResponse(Response):
    def __init__(self):
        super().__init__(
            4678,
            0)

class SubscribeAllEventsResponse(Response):
    def __init__(self):
        super().__init__(
            4678,
            10)

class AddTaskResponse(Response):
    def __init__(self):
        super().__init__(
            4690,
            7)

class CommitTaskTransactionResponse(Response):
    def __init__(self):
        super().__init__(
            4690,
            11)

class DeleteAllTasksResponse(Response):
    def __init__(self):
        super().__init__(
            4690,
            9)

class DeleteTaskResponse(Response):
    def __init__(self):
        super().__init__(
            4690,
            8)

class GetNumberOfTasksResponse(Response):
    number_of_tasks: int

    def __init__(self, number_of_tasks: int = 0):
        self.number_of_tasks = number_of_tasks
        super().__init__(
            4690,
            4,
            [
                Parameter("number_of_tasks", "u32"),
            ])

class GetTaskResponse(Response):
    start: int
    duration: int
    use_on_monday: bool
    use_on_tuesday: bool
    use_on_wednesday: bool
    use_on_thursday: bool
    use_on_friday: bool
    use_on_saturday: bool
    use_on_sunday: bool

    def __init__(self, start: int = 0, duration: int = 0, use_on_monday: bool = False, use_on_tuesday: bool = False, use_on_wednesday: bool = False, use_on_thursday: bool = False, use_on_friday: bool = False, use_on_saturday: bool = False, use_on_sunday: bool = False):
        self.start = start
        self.duration = duration
        self.use_on_monday = use_on_monday
        self.use_on_tuesday = use_on_tuesday
        self.use_on_wednesday = use_on_wednesday
        self.use_on_thursday = use_on_thursday
        self.use_on_friday = use_on_friday
        self.use_on_saturday = use_on_saturday
        self.use_on_sunday = use_on_sunday
        super().__init__(
            4690,
            5,
            [
                Parameter("start", "u32"),
                Parameter("duration", "u32"),
                Parameter("use_on_monday", "bool"),
                Parameter("use_on_tuesday", "bool"),
                Parameter("use_on_wednesday", "bool"),
                Parameter("use_on_thursday", "bool"),
                Parameter("use_on_friday", "bool"),
                Parameter("use_on_saturday", "bool"),
                Parameter("use_on_sunday", "bool"),
            ])

class GetTimeResponse(Response):
    time: int

    def __init__(self, time: int = 0):
        self.time = time
        super().__init__(
            4690,
            2,
            [
                Parameter("time", "u32"),
            ])

class SetTaskResponse(Response):
    def __init__(self):
        super().__init__(
            4690,
            6)

class SetTimeResponse(Response):
    def __init__(self):
        super().__init__(
            4690,
            3)

class StartTaskTransactionResponse(Response):
    def __init__(self):
        super().__init__(
            4690,
            10)

class SubscribeAllEventsResponse(Response):
    def __init__(self):
        super().__init__(
            4690,
            0)

class SubscribeEventChannelResponse(Response):
    def __init__(self):
        super().__init__(
            4690,
            1)

class ChargingGateOffResponse(Response):
    def __init__(self):
        super().__init__(
            4486,
            1)

class ChargingGateOnResponse(Response):
    def __init__(self):
        super().__init__(
            4486,
            2)

class ChargingOffResponse(Response):
    def __init__(self):
        super().__init__(
            4486,
            0)

class GetChargingErrorCountResponse(Response):
    charging_errors: int

    def __init__(self, charging_errors: int = 0):
        self.charging_errors = charging_errors
        super().__init__(
            5512,
            24,
            [
                Parameter("charging_errors", "u8"),
            ])

class GetChargingPowerDetectedCountResponse(Response):
    detection_count: int

    def __init__(self, detection_count: int = 0):
        self.detection_count = detection_count
        super().__init__(
            5512,
            21,
            [
                Parameter("detection_count", "s32"),
            ])

class GetCurrentChargingTimeMaxResponse(Response):
    time: int

    def __init__(self, time: int = 0):
        self.time = time
        super().__init__(
            5512,
            19,
            [
                Parameter("time", "u32"),
            ])

class GetCurrentChargingTimeResponse(Response):
    time: int

    def __init__(self, time: int = 0):
        self.time = time
        super().__init__(
            5512,
            15,
            [
                Parameter("time", "u32"),
            ])

class GetIsBatteryChargingPreventedResponse(Response):
    is_battery_charging_prevented: bool

    def __init__(self, is_battery_charging_prevented: bool = False):
        self.is_battery_charging_prevented = is_battery_charging_prevented
        super().__init__(
            5512,
            10,
            [
                Parameter("is_battery_charging_prevented", "bool"),
            ])

class GetIsBatteryChargingResponse(Response):
    is_battery_charging: bool

    def __init__(self, is_battery_charging: bool = False):
        self.is_battery_charging = is_battery_charging
        super().__init__(
            5512,
            8,
            [
                Parameter("is_battery_charging", "bool"),
            ])

class GetIsChargingPowerDetectedResponse(Response):
    is_detected: bool

    def __init__(self, is_detected: bool = False):
        self.is_detected = is_detected
        super().__init__(
            5512,
            7,
            [
                Parameter("is_detected", "bool"),
            ])

class GetIsChargingPreventedResponse(Response):
    is_charging_prevented: bool

    def __init__(self, is_charging_prevented: bool = False):
        self.is_charging_prevented = is_charging_prevented
        super().__init__(
            5512,
            11,
            [
                Parameter("is_charging_prevented", "bool"),
            ])

class GetIsChargingResponse(Response):
    is_charging: bool

    def __init__(self, is_charging: bool = False):
        self.is_charging = is_charging
        super().__init__(
            5512,
            9,
            [
                Parameter("is_charging", "bool"),
            ])

class GetIsInChargingStateResponse(Response):
    is_in_charging_state: bool

    def __init__(self, is_in_charging_state: bool = False):
        self.is_in_charging_state = is_in_charging_state
        super().__init__(
            5512,
            14,
            [
                Parameter("is_in_charging_state", "bool"),
            ])

class GetLastChargingTimeMaxResponse(Response):
    time: int

    def __init__(self, time: int = 0):
        self.time = time
        super().__init__(
            5512,
            20,
            [
                Parameter("time", "u32"),
            ])

class GetLastChargingTimeResponse(Response):
    time: int

    def __init__(self, time: int = 0):
        self.time = time
        super().__init__(
            5512,
            18,
            [
                Parameter("time", "u32"),
            ])

class GetRemainingChargingTimeResponse(Response):
    time: int

    def __init__(self, time: int = 0):
        self.time = time
        super().__init__(
            5512,
            16,
            [
                Parameter("time", "u32"),
            ])

class GetRemainingTotalChargingTimeResponse(Response):
    time: int

    def __init__(self, time: int = 0):
        self.time = time
        super().__init__(
            5512,
            17,
            [
                Parameter("time", "u32"),
            ])

class GetSimChargingGateResponse(Response):
    enabled: bool

    def __init__(self, enabled: bool = False):
        self.enabled = enabled
        super().__init__(
            5512,
            2,
            [
                Parameter("enabled", "bool"),
            ])

class GetSimExtPowerDetectedResponse(Response):
    detected: bool

    def __init__(self, detected: bool = False):
        self.detected = detected
        super().__init__(
            5512,
            4,
            [
                Parameter("detected", "bool"),
            ])

class GetSimIsChargingEnabledResponse(Response):
    sim_is_charging_enabled: bool

    def __init__(self, sim_is_charging_enabled: bool = False):
        self.sim_is_charging_enabled = sim_is_charging_enabled
        super().__init__(
            5744,
            5,
            [
                Parameter("sim_is_charging_enabled", "bool"),
            ])

class GetSimIsPowerConnectedResponse(Response):
    sim_is_power_connected: bool

    def __init__(self, sim_is_power_connected: bool = False):
        self.sim_is_power_connected = sim_is_power_connected
        super().__init__(
            5744,
            3,
            [
                Parameter("sim_is_power_connected", "bool"),
            ])

class GetSimulationResponse(Response):
    sim_on: bool

    def __init__(self, sim_on: bool = False):
        self.sim_on = sim_on
        super().__init__(
            5512,
            1,
            [
                Parameter("sim_on", "bool"),
            ])

class GetStateResponse(Response):
    state: int

    def __init__(self, state: int = 0):
        self.state = state
        super().__init__(
            5512,
            12,
            [
                Parameter("state", "u8"),
            ])

class GetStatusResponse(Response):
    status: int

    def __init__(self, status: int = 0):
        self.status = status
        super().__init__(
            4486,
            8,
            [
                Parameter("status", "u32"),
            ])

class GetSubStateResponse(Response):
    sub_state: int

    def __init__(self, sub_state: int = 0):
        self.sub_state = sub_state
        super().__init__(
            5512,
            13,
            [
                Parameter("sub_state", "u8"),
            ])

class InjectChargingErrorResponse(Response):
    def __init__(self):
        super().__init__(
            5512,
            6)

class IsChargingEnabledResponse(Response):
    is_charging_enabled: bool

    def __init__(self, is_charging_enabled: bool = False):
        self.is_charging_enabled = is_charging_enabled
        super().__init__(
            4486,
            3,
            [
                Parameter("is_charging_enabled", "bool"),
            ])

class IsChargingPowerConnectedResponse(Response):
    is_charging_power_connected: bool

    def __init__(self, is_charging_power_connected: bool = False):
        self.is_charging_power_connected = is_charging_power_connected
        super().__init__(
            4486,
            4,
            [
                Parameter("is_charging_power_connected", "bool"),
            ])

class IsChargingPrevetnedResponse(Response):
    is_charging_prevented: bool

    def __init__(self, is_charging_prevented: bool = False):
        self.is_charging_prevented = is_charging_prevented
        super().__init__(
            4486,
            6,
            [
                Parameter("is_charging_prevented", "bool"),
            ])

class IsReadyResponse(Response):
    is_ready: bool

    def __init__(self, is_ready: bool = False):
        self.is_ready = is_ready
        super().__init__(
            4486,
            9,
            [
                Parameter("is_ready", "bool"),
            ])

class PreventChargingResponse(Response):
    def __init__(self):
        super().__init__(
            4486,
            5)

class PreventSingleChargingResponse(Response):
    def __init__(self):
        super().__init__(
            5512,
            22)

class ResetStatusResponse(Response):
    def __init__(self):
        super().__init__(
            5512,
            23)

class SetSimChargingGateResponse(Response):
    def __init__(self):
        super().__init__(
            5512,
            3)

class SetSimExtPowerDetectedResponse(Response):
    def __init__(self):
        super().__init__(
            5512,
            5)

class SetSimIsChargingEnabledResponse(Response):
    sim_is_charging_enabled: bool

    def __init__(self, sim_is_charging_enabled: bool = False):
        self.sim_is_charging_enabled = sim_is_charging_enabled
        super().__init__(
            5744,
            4,
            [
                Parameter("sim_is_charging_enabled", "bool"),
            ])

class SetSimIsPowerConnectedResponse(Response):
    sim_is_power_connected: bool

    def __init__(self, sim_is_power_connected: bool = False):
        self.sim_is_power_connected = sim_is_power_connected
        super().__init__(
            5744,
            2,
            [
                Parameter("sim_is_power_connected", "bool"),
            ])

class SetSimulationResponse(Response):
    sim_on: bool

    def __init__(self, sim_on: bool = False):
        self.sim_on = sim_on
        super().__init__(
            5512,
            0,
            [
                Parameter("sim_on", "bool"),
            ])

class SubscribeAllEventsResponse(Response):
    def __init__(self):
        super().__init__(
            4486,
            7)

class GetAllSettingsResponse(Response):
    eco_mode_enabled: bool
    mower_house_installed: bool

    def __init__(self, eco_mode_enabled: bool = False, mower_house_installed: bool = False):
        self.eco_mode_enabled = eco_mode_enabled
        self.mower_house_installed = mower_house_installed
        super().__init__(
            4692,
            10,
            [
                Parameter("eco_mode_enabled", "bool"),
                Parameter("mower_house_installed", "bool"),
            ])

class GetEcoModeEnabledResponse(Response):
    eco_mode_enabled: bool

    def __init__(self, eco_mode_enabled: bool = False):
        self.eco_mode_enabled = eco_mode_enabled
        super().__init__(
            4692,
            6,
            [
                Parameter("eco_mode_enabled", "bool"),
            ])

class GetMowerHouseInstalledResponse(Response):
    mower_house_installed: bool

    def __init__(self, mower_house_installed: bool = False):
        self.mower_house_installed = mower_house_installed
        super().__init__(
            4692,
            4,
            [
                Parameter("mower_house_installed", "bool"),
            ])

class InitiateNewPairingResponse(Response):
    def __init__(self):
        super().__init__(
            4692,
            2)

class SetEcoModeEnabledResponse(Response):
    def __init__(self):
        super().__init__(
            4692,
            5)

class SetMowerHouseInstalledResponse(Response):
    def __init__(self):
        super().__init__(
            4692,
            3)

class SubscribeAllEventsResponse(Response):
    def __init__(self):
        super().__init__(
            4692,
            11)

class SubscribeEventChannelResponse(Response):
    def __init__(self):
        super().__init__(
            4692,
            12)

class GetAllSettingsResponse(Response):
    drive_past_wire: int

    def __init__(self, drive_past_wire: int = 0):
        self.drive_past_wire = drive_past_wire
        super().__init__(
            4712,
            2,
            [
                Parameter("drive_past_wire", "u16"),
            ])

class GetDrivePastWireResponse(Response):
    distance: int

    def __init__(self, distance: int = 0):
        self.distance = distance
        super().__init__(
            4712,
            0,
            [
                Parameter("distance", "u16"),
            ])

class SetDrivePastWireResponse(Response):
    def __init__(self):
        super().__init__(
            4712,
            1)

class SubscribeAllEventsResponse(Response):
    def __init__(self):
        super().__init__(
            4712,
            9)

class GetBoundaryCorridorResponse(Response):
    max: int

    def __init__(self, max: int = 0):
        self.max = max
        super().__init__(
            4706,
            24,
            [
                Parameter("max", "u8"),
            ])

class GetCurrentDistanceResponse(Response):
    distance: int

    def __init__(self, distance: int = 0):
        self.distance = distance
        super().__init__(
            4706,
            16,
            [
                Parameter("distance", "u16"),
            ])

class GetNumberOfGuidesResponse(Response):
    number_of_guides: int

    def __init__(self, number_of_guides: int = 0):
        self.number_of_guides = number_of_guides
        super().__init__(
            4706,
            14,
            [
                Parameter("number_of_guides", "u8"),
            ])

class GetPassageCuttingEnabledResponse(Response):
    passage_cutting_enabled: bool

    def __init__(self, passage_cutting_enabled: bool = False):
        self.passage_cutting_enabled = passage_cutting_enabled
        super().__init__(
            4706,
            26,
            [
                Parameter("passage_cutting_enabled", "bool"),
            ])

class GetStartingPointDistanceResponse(Response):
    distance: int

    def __init__(self, distance: int = 0):
        self.distance = distance
        super().__init__(
            4706,
            10,
            [
                Parameter("distance", "u16"),
            ])

class GetStartingPointEnabledResponse(Response):
    enabled: bool

    def __init__(self, enabled: bool = False):
        self.enabled = enabled
        super().__init__(
            4706,
            6,
            [
                Parameter("enabled", "bool"),
            ])

class GetStartingPointMaxResponse(Response):
    starting_point_max: int

    def __init__(self, starting_point_max: int = 0):
        self.starting_point_max = starting_point_max
        super().__init__(
            4706,
            28,
            [
                Parameter("starting_point_max", "u8"),
            ])

class GetStartingPointProportionResponse(Response):
    proportion: int

    def __init__(self, proportion: int = 0):
        self.proportion = proportion
        super().__init__(
            4706,
            12,
            [
                Parameter("proportion", "u8"),
            ])

class GetStartingPointSettingsResponse(Response):
    enabled: bool
    proportion: int
    wire: int
    distance: int
    passage_cutting_enabled: bool

    def __init__(self, enabled: bool = False, proportion: int = 0, wire: int = 0, distance: int = 0, passage_cutting_enabled: bool = False):
        self.enabled = enabled
        self.proportion = proportion
        self.wire = wire
        self.distance = distance
        self.passage_cutting_enabled = passage_cutting_enabled
        super().__init__(
            4706,
            21,
            [
                Parameter("enabled", "bool"),
                Parameter("proportion", "u8"),
                Parameter("wire", "u8"),
                Parameter("distance", "u16"),
                Parameter("passage_cutting_enabled", "bool"),
            ])

class GetStartingPointWireResponse(Response):
    wire: int

    def __init__(self, wire: int = 0):
        self.wire = wire
        super().__init__(
            4706,
            8,
            [
                Parameter("wire", "u8"),
            ])

class GetTestErrorResponse(Response):
    error: int

    def __init__(self, error: int = 0):
        self.error = error
        super().__init__(
            4706,
            29,
            [
                Parameter("error", "u8"),
            ])

class GetTestModeResponse(Response):
    mode: int

    def __init__(self, mode: int = 0):
        self.mode = mode
        super().__init__(
            4706,
            22,
            [
                Parameter("mode", "u8"),
            ])

class GetTestStateResponse(Response):
    state: int

    def __init__(self, state: int = 0):
        self.state = state
        super().__init__(
            4706,
            23,
            [
                Parameter("state", "u8"),
            ])

class SetBoundaryCorridorResponse(Response):
    def __init__(self):
        super().__init__(
            4706,
            25)

class SetPassageCuttingEnabledResponse(Response):
    def __init__(self):
        super().__init__(
            4706,
            27)

class SetStartingPointDistanceResponse(Response):
    def __init__(self):
        super().__init__(
            4706,
            11)

class SetStartingPointEnabledResponse(Response):
    def __init__(self):
        super().__init__(
            4706,
            7)

class SetStartingPointProportionResponse(Response):
    def __init__(self):
        super().__init__(
            4706,
            13)

class SetStartingPointWireResponse(Response):
    def __init__(self):
        super().__init__(
            4706,
            9)

class SubscribeAllEventsResponse(Response):
    def __init__(self):
        super().__init__(
            4706,
            19)

class SubscribeEventChannelResponse(Response):
    def __init__(self):
        super().__init__(
            4706,
            20)

class TestAbortResponse(Response):
    def __init__(self):
        super().__init__(
            4706,
            18)

class TestFollowInResponse(Response):
    def __init__(self):
        super().__init__(
            4706,
            17)

class TestStartingPointResponse(Response):
    def __init__(self):
        super().__init__(
            4706,
            15)

class GetAllSettingsResponse(Response):
    available: bool
    enabled: bool

    def __init__(self, available: bool = False, enabled: bool = False):
        self.available = available
        self.enabled = enabled
        super().__init__(
            5370,
            8,
            [
                Parameter("available", "bool"),
                Parameter("enabled", "bool"),
            ])

class GetAvailableResponse(Response):
    available: bool

    def __init__(self, available: bool = False):
        self.available = available
        super().__init__(
            5370,
            0,
            [
                Parameter("available", "bool"),
            ])

class GetEnabledResponse(Response):
    enabled: bool

    def __init__(self, enabled: bool = False):
        self.enabled = enabled
        super().__init__(
            5412,
            1,
            [
                Parameter("enabled", "bool"),
            ])

class GetEnabledResponseOBP(Response):
    enabled: bool

    def __init__(self, enabled: bool = False):
        self.enabled = enabled
        super().__init__(
            5370,
            1,
            [
                Parameter("enabled", "bool"),
            ])

class SetEnabledResponse(Response):
    def __init__(self):
        super().__init__(
            5412,
            2)

class SetEnabledResponseOBP(Response):
    def __init__(self):
        super().__init__(
            5370,
            2)

class SubscribeAllEventsResponse(Response):
    def __init__(self):
        super().__init__(
            5370,
            9)

class ClearSettingsResponse(Response):
    def __init__(self):
        super().__init__(
            4462,
            18)

class GetCloseToBoundaryLimitResponse(Response):
    close_to_boundary_limit: int

    def __init__(self, close_to_boundary_limit: int = 0):
        self.close_to_boundary_limit = close_to_boundary_limit
        super().__init__(
            4462,
            5,
            [
                Parameter("close_to_boundary_limit", "s16"),
            ])

class GetCloseToBoundaryOffsetResponse(Response):
    close_to_boundary_offset: int

    def __init__(self, close_to_boundary_offset: int = 0):
        self.close_to_boundary_offset = close_to_boundary_offset
        super().__init__(
            4462,
            6,
            [
                Parameter("close_to_boundary_offset", "u16"),
            ])

class GetCloseToBoundaryResponse(Response):
    is_close_to_boundary: bool

    def __init__(self, is_close_to_boundary: bool = False):
        self.is_close_to_boundary = is_close_to_boundary
        super().__init__(
            4290,
            1,
            [
                Parameter("is_close_to_boundary", "bool"),
            ])

class GetCloseToCsLimitResponse(Response):
    close_to_cs_limit: int

    def __init__(self, close_to_cs_limit: int = 0):
        self.close_to_cs_limit = close_to_cs_limit
        super().__init__(
            4462,
            30,
            [
                Parameter("close_to_cs_limit", "s16"),
            ])

class GetCloseToCsOffsetResponse(Response):
    close_to_cs_offset: int

    def __init__(self, close_to_cs_offset: int = 0):
        self.close_to_cs_offset = close_to_cs_offset
        super().__init__(
            4462,
            31,
            [
                Parameter("close_to_cs_offset", "u16"),
            ])

class GetCloseToCsResponse(Response):
    is_close_to_cs: bool

    def __init__(self, is_close_to_cs: bool = False):
        self.is_close_to_cs = is_close_to_cs
        super().__init__(
            4290,
            0,
            [
                Parameter("is_close_to_cs", "bool"),
            ])

class GetInstalledLoopsResponse(Response):
    a: bool
    f: bool
    n: bool
    g1: bool
    g2: bool
    g3: bool

    def __init__(self, a: bool = False, f: bool = False, n: bool = False, g1: bool = False, g2: bool = False, g3: bool = False):
        self.a = a
        self.f = f
        self.n = n
        self.g1 = g1
        self.g2 = g2
        self.g3 = g3
        super().__init__(
            4462,
            29,
            [
                Parameter("a", "bool"),
                Parameter("f", "bool"),
                Parameter("n", "bool"),
                Parameter("g1", "bool"),
                Parameter("g2", "bool"),
                Parameter("g3", "bool"),
            ])

class GetLoopSideResponse(Response):
    side: int

    def __init__(self, side: int = 0):
        self.side = side
        super().__init__(
            4462,
            33,
            [
                Parameter("side", "u8"),
            ])

class GetLoopSignalResponse(Response):
    loop_signal: int

    def __init__(self, loop_signal: int = 0):
        self.loop_signal = loop_signal
        super().__init__(
            4462,
            12,
            [
                Parameter("loop_signal", "s16"),
            ])

class GetLoopSignalsResponse(Response):
    loop_signal_a: int
    loop_signal_f: int
    loop_signal_n: int
    loop_signal_g1: int
    loop_signal_g2: int
    loop_signal_g3: int

    def __init__(self, loop_signal_a: int = 0, loop_signal_f: int = 0, loop_signal_n: int = 0, loop_signal_g1: int = 0, loop_signal_g2: int = 0, loop_signal_g3: int = 0):
        self.loop_signal_a = loop_signal_a
        self.loop_signal_f = loop_signal_f
        self.loop_signal_n = loop_signal_n
        self.loop_signal_g1 = loop_signal_g1
        self.loop_signal_g2 = loop_signal_g2
        self.loop_signal_g3 = loop_signal_g3
        super().__init__(
            4462,
            13,
            [
                Parameter("loop_signal_a", "s16"),
                Parameter("loop_signal_f", "s16"),
                Parameter("loop_signal_n", "s16"),
                Parameter("loop_signal_g1", "s16"),
                Parameter("loop_signal_g2", "s16"),
                Parameter("loop_signal_g3", "s16"),
            ])

class GetMinMaxResponse(Response):
    a_max_level: int
    a_maxconfidence: int
    a_max_fast_level: int
    a_max_fast_confidence: int
    g1_min_level: int
    g1_min_confidence: int
    g2_min_level: int
    g2_min_confidence: int
    g3_min_level: int
    g3_min_confidence: int

    def __init__(self, a_max_level: int = 0, a_maxconfidence: int = 0, a_max_fast_level: int = 0, a_max_fast_confidence: int = 0, g1_min_level: int = 0, g1_min_confidence: int = 0, g2_min_level: int = 0, g2_min_confidence: int = 0, g3_min_level: int = 0, g3_min_confidence: int = 0):
        self.a_max_level = a_max_level
        self.a_maxconfidence = a_maxconfidence
        self.a_max_fast_level = a_max_fast_level
        self.a_max_fast_confidence = a_max_fast_confidence
        self.g1_min_level = g1_min_level
        self.g1_min_confidence = g1_min_confidence
        self.g2_min_level = g2_min_level
        self.g2_min_confidence = g2_min_confidence
        self.g3_min_level = g3_min_level
        self.g3_min_confidence = g3_min_confidence
        super().__init__(
            4462,
            8,
            [
                Parameter("a_max_level", "s16"),
                Parameter("a_maxconfidence", "u8"),
                Parameter("a_max_fast_level", "s16"),
                Parameter("a_max_fast_confidence", "u8"),
                Parameter("g1_min_level", "s16"),
                Parameter("g1_min_confidence", "u8"),
                Parameter("g2_min_level", "s16"),
                Parameter("g2_min_confidence", "u8"),
                Parameter("g3_min_level", "s16"),
                Parameter("g3_min_confidence", "u8"),
            ])

class GetNbrAvailableGuidesResponse(Response):
    nbr_guides: int

    def __init__(self, nbr_guides: int = 0):
        self.nbr_guides = nbr_guides
        super().__init__(
            4462,
            22,
            [
                Parameter("nbr_guides", "u8"),
            ])

class GetNoLoopStatusResponse(Response):
    mask: int

    def __init__(self, mask: int = 0):
        self.mask = mask
        super().__init__(
            4462,
            4,
            [
                Parameter("mask", "u32"),
            ])

class GetNumSensorsResponse(Response):
    num_sensors: int

    def __init__(self, num_sensors: int = 0):
        self.num_sensors = num_sensors
        super().__init__(
            4462,
            11,
            [
                Parameter("num_sensors", "u8"),
            ])

class GetOnCsStatusResponse(Response):
    mask: int

    def __init__(self, mask: int = 0):
        self.mask = mask
        super().__init__(
            4462,
            3,
            [
                Parameter("mask", "u32"),
            ])

class GetOutsideStatusResponse(Response):
    mask: int

    def __init__(self, mask: int = 0):
        self.mask = mask
        super().__init__(
            4462,
            2,
            [
                Parameter("mask", "u32"),
            ])

class GetPeakUpdateActiveResponse(Response):
    active: bool

    def __init__(self, active: bool = False):
        self.active = active
        super().__init__(
            4462,
            16,
            [
                Parameter("active", "bool"),
            ])

class GetPeriodTimeResponse(Response):
    period_time: int

    def __init__(self, period_time: int = 0):
        self.period_time = period_time
        super().__init__(
            4462,
            9,
            [
                Parameter("period_time", "u16"),
            ])

class GetRawLoopSignalResponse(Response):
    loop_signal: int

    def __init__(self, loop_signal: int = 0):
        self.loop_signal = loop_signal
        super().__init__(
            4462,
            24,
            [
                Parameter("loop_signal", "s16"),
            ])

class GetRawLoopSignalsResponse(Response):
    loop_signal_a: int
    loop_signal_f: int
    loop_signal_n: int
    loop_signal_g1: int
    loop_signal_g2: int
    loop_signal_g3: int

    def __init__(self, loop_signal_a: int = 0, loop_signal_f: int = 0, loop_signal_n: int = 0, loop_signal_g1: int = 0, loop_signal_g2: int = 0, loop_signal_g3: int = 0):
        self.loop_signal_a = loop_signal_a
        self.loop_signal_f = loop_signal_f
        self.loop_signal_n = loop_signal_n
        self.loop_signal_g1 = loop_signal_g1
        self.loop_signal_g2 = loop_signal_g2
        self.loop_signal_g3 = loop_signal_g3
        super().__init__(
            4462,
            25,
            [
                Parameter("loop_signal_a", "s16"),
                Parameter("loop_signal_f", "s16"),
                Parameter("loop_signal_n", "s16"),
                Parameter("loop_signal_g1", "s16"),
                Parameter("loop_signal_g2", "s16"),
                Parameter("loop_signal_g3", "s16"),
            ])

class GetSignalQualityResponse(Response):
    signal_quality: int

    def __init__(self, signal_quality: int = 0):
        self.signal_quality = signal_quality
        super().__init__(
            4462,
            14,
            [
                Parameter("signal_quality", "u8"),
            ])

class GetSyncSensitivityResponse(Response):
    sensitivity: int

    def __init__(self, sensitivity: int = 0):
        self.sensitivity = sensitivity
        super().__init__(
            4462,
            26,
            [
                Parameter("sensitivity", "u8"),
            ])

class GetTemporaryPeriodTimeResponse(Response):
    temporary_period_time: int

    def __init__(self, temporary_period_time: int = 0):
        self.temporary_period_time = temporary_period_time
        super().__init__(
            4462,
            20,
            [
                Parameter("temporary_period_time", "u16"),
            ])

class IsOnCsResponse(Response):
    is_on_cs: bool

    def __init__(self, is_on_cs: bool = False):
        self.is_on_cs = is_on_cs
        super().__init__(
            4462,
            1,
            [
                Parameter("is_on_cs", "bool"),
            ])

class IsOutsideResponse(Response):
    is_outside: bool

    def __init__(self, is_outside: bool = False):
        self.is_outside = is_outside
        super().__init__(
            4462,
            0,
            [
                Parameter("is_outside", "bool"),
            ])

class IsParkRequestedResponse(Response):
    park_requested: bool

    def __init__(self, park_requested: bool = False):
        self.park_requested = park_requested
        super().__init__(
            4462,
            19,
            [
                Parameter("park_requested", "bool"),
            ])

class IsReadyResponse(Response):
    is_ready: bool

    def __init__(self, is_ready: bool = False):
        self.is_ready = is_ready
        super().__init__(
            4462,
            28,
            [
                Parameter("is_ready", "bool"),
            ])

class SetCloseToBoundaryOffsetResponse(Response):
    def __init__(self):
        super().__init__(
            4462,
            7)

class SetCloseToCsOffsetResponse(Response):
    def __init__(self):
        super().__init__(
            4462,
            32)

class SetNbrAvailableGuidesResponse(Response):
    def __init__(self):
        super().__init__(
            4462,
            23)

class SetPeakUpdateActiveResponse(Response):
    def __init__(self):
        super().__init__(
            4462,
            17)

class SetPeakValueResponse(Response):
    def __init__(self):
        super().__init__(
            4462,
            15)

class SetPeriodTimeResponse(Response):
    def __init__(self):
        super().__init__(
            4462,
            10)

class SetSyncSensitivityResponse(Response):
    def __init__(self):
        super().__init__(
            4462,
            27)

class SetTemporaryPeriodTimeResponse(Response):
    def __init__(self):
        super().__init__(
            4462,
            21)

class GetMessageResponse(Response):
    time: int
    code: int
    severity: int

    def __init__(self, time: int = 0, code: int = 0, severity: int = 0):
        self.time = time
        self.code = code
        self.severity = severity
        super().__init__(
            4730,
            1,
            [
                Parameter("time", "u32"),
                Parameter("code", "u32"),
                Parameter("severity", "u8"),
            ])

class GetNumberOfMessagesResponse(Response):
    number_of_messages: int

    def __init__(self, number_of_messages: int = 0):
        self.number_of_messages = number_of_messages
        super().__init__(
            4730,
            0,
            [
                Parameter("number_of_messages", "u32"),
            ])

class ConfirmErrorResponse(Response):
    def __init__(self):
        super().__init__(
            4586,
            9)

class GetActivityResponse(Response):
    mower_activity: int

    def __init__(self, mower_activity: int = 0):
        self.mower_activity = mower_activity
        super().__init__(
            4586,
            3,
            [
                Parameter("mower_activity", "u8"),
            ])

class GetErrorResponse(Response):
    error_code: int

    def __init__(self, error_code: int = 0):
        self.error_code = error_code
        super().__init__(
            4586,
            6,
            [
                Parameter("error_code", "u32"),
            ])

class GetForceDemoModeResponse(Response):
    enable: bool

    def __init__(self, enable: bool = False):
        self.enable = enable
        super().__init__(
            4586,
            102,
            [
                Parameter("enable", "bool"),
            ])

class GetInternalStateResponse(Response):
    state: int

    def __init__(self, state: int = 0):
        self.state = state
        super().__init__(
            4586,
            100,
            [
                Parameter("state", "u8"),
            ])

class GetMissionResponse(Response):
    mission_id: int

    def __init__(self, mission_id: int = 0):
        self.mission_id = mission_id
        super().__init__(
            4586,
            13,
            [
                Parameter("mission_id", "u32"),
            ])

class GetModeResponse(Response):
    mode_of_operation: int

    def __init__(self, mode_of_operation: int = 0):
        self.mode_of_operation = mode_of_operation
        super().__init__(
            4586,
            1,
            [
                Parameter("mode_of_operation", "u8"),
            ])

class GetRestrictedResponse(Response):
    restricted: bool

    def __init__(self, restricted: bool = False):
        self.restricted = restricted
        super().__init__(
            4586,
            11,
            [
                Parameter("restricted", "bool"),
            ])

class GetStateResponse(Response):
    mower_state: int

    def __init__(self, mower_state: int = 0):
        self.mower_state = mower_state
        super().__init__(
            4586,
            2,
            [
                Parameter("mower_state", "u8"),
            ])

class IsErrorConfirmableResponse(Response):
    confirmable: bool

    def __init__(self, confirmable: bool = False):
        self.confirmable = confirmable
        super().__init__(
            4586,
            8,
            [
                Parameter("confirmable", "bool"),
            ])

class IsWaitingForStartTriggerResponse(Response):
    is_waiting: bool

    def __init__(self, is_waiting: bool = False):
        self.is_waiting = is_waiting
        super().__init__(
            4586,
            14,
            [
                Parameter("is_waiting", "bool"),
            ])

class PauseResponse(Response):
    def __init__(self):
        super().__init__(
            4586,
            5)

class SetForceDemoModeResponse(Response):
    def __init__(self):
        super().__init__(
            4586,
            101)

class SetMissionResponse(Response):
    def __init__(self):
        super().__init__(
            4586,
            12)

class SetModeResponse(Response):
    def __init__(self):
        super().__init__(
            4586,
            0)

class SetRestrictedResponse(Response):
    def __init__(self):
        super().__init__(
            4586,
            10)

class StartTriggerResponse(Response):
    def __init__(self):
        super().__init__(
            4586,
            4)

class SubscribeAllEventsResponse(Response):
    def __init__(self):
        super().__init__(
            4586,
            7)

class ClearOverrideResponse(Response):
    def __init__(self):
        super().__init__(
            4658,
            6)

class GetNextStartTimeResponse(Response):
    next_start_time: int

    def __init__(self, next_start_time: int = 0):
        self.next_start_time = next_start_time
        super().__init__(
            4658,
            1,
            [
                Parameter("next_start_time", "u32"),
            ])

class GetOverrideResponse(Response):
    action: int
    start_time: int
    duration: int

    def __init__(self, action: int = 0, start_time: int = 0, duration: int = 0):
        self.action = action
        self.start_time = start_time
        self.duration = duration
        super().__init__(
            4658,
            2,
            [
                Parameter("action", "u8"),
                Parameter("start_time", "u32"),
                Parameter("duration", "u32"),
            ])

class GetRestrictionReasonResponse(Response):
    restriction_reason: int

    def __init__(self, restriction_reason: int = 0):
        self.restriction_reason = restriction_reason
        super().__init__(
            4658,
            0,
            [
                Parameter("restriction_reason", "u8"),
            ])

class SetOverrideMowResponse(Response):
    def __init__(self):
        super().__init__(
            4658,
            3)

class SetOverrideParkResponse(Response):
    def __init__(self):
        super().__init__(
            4658,
            4)

class SetOverrideParkUntilNextStartResponse(Response):
    def __init__(self):
        super().__init__(
            4658,
            5)

class AbortResponse(Response):
    def __init__(self):
        super().__init__(
            4710,
            8)

class GetAllSettingsResponse(Response):
    enabled: bool
    sensitivity: int
    available: bool

    def __init__(self, enabled: bool = False, sensitivity: int = 0, available: bool = False):
        self.enabled = enabled
        self.sensitivity = sensitivity
        self.available = available
        super().__init__(
            4710,
            5,
            [
                Parameter("enabled", "bool"),
                Parameter("sensitivity", "u8"),
                Parameter("available", "bool"),
            ])

class GetAutoTrigCurrentResponse(Response):
    trig_current: int

    def __init__(self, trig_current: int = 0):
        self.trig_current = trig_current
        super().__init__(
            5772,
            9,
            [
                Parameter("trig_current", "s32"),
            ])

class GetAutoTrigIntensityResponse(Response):
    trig_intensity: int

    def __init__(self, trig_intensity: int = 0):
        self.trig_intensity = trig_intensity
        super().__init__(
            5772,
            10,
            [
                Parameter("trig_intensity", "s32"),
            ])

class GetAvailableResponse(Response):
    available: bool

    def __init__(self, available: bool = False):
        self.available = available
        super().__init__(
            4710,
            0,
            [
               Parameter("available", "bool"),
            ])

class GetDetailedLogEnabledResponse(Response):
    enabled: bool

    def __init__(self, enabled: bool = False):
        self.enabled = enabled
        super().__init__(
            5772,
            1,
            [
                Parameter("enabled", "bool"),
            ])

class GetEnabledResponse(Response):
    enabled: bool

    def __init__(self, enabled: bool = False):
        self.enabled = enabled
        super().__init__(
            4710,
            1,
            [
                Parameter("enabled", "bool"),
            ])

class GetMeanCutCurrentResponse(Response):
    mean_cut_current_value: int
    mean_cut_current_confidence: int

    def __init__(self, mean_cut_current_value: int = 0, mean_cut_current_confidence: int = 0):
        self.mean_cut_current_value = mean_cut_current_value
        self.mean_cut_current_confidence = mean_cut_current_confidence
        super().__init__(
            5772,
            5,
            [
                Parameter("mean_cut_current_value", "s32"),
                Parameter("mean_cut_current_confidence", "u8"),
            ])

class GetMeanCutIntensityResponse(Response):
    mean_cut_intensity_value: int
    mean_cut_intensity_confidence: int

    def __init__(self, mean_cut_intensity_value: int = 0, mean_cut_intensity_confidence: int = 0):
        self.mean_cut_intensity_value = mean_cut_intensity_value
        self.mean_cut_intensity_confidence = mean_cut_intensity_confidence
        super().__init__(
            5772,
            6,
            [
                Parameter("mean_cut_intensity_value", "s32"),
                Parameter("mean_cut_intensity_confidence", "u8"),
            ])

class GetSensitivityResponse(Response):
    sensitivity: int

    def __init__(self, sensitivity: int = 0):
        self.sensitivity = sensitivity
        super().__init__(
            4710,
            3,
            [
                Parameter("sensitivity", "u8"),
            ])

class GetStateResponse(Response):
    state: int

    def __init__(self, state: int = 0):
        self.state = state
        super().__init__(
            5772,
            0,
            [
                Parameter("state", "u8"),
            ])

class GetStatusResponse(Response):
    status: int

    def __init__(self, status: int = 0):
        self.status = status
        super().__init__(
            4710,
            9,
            [
                Parameter("status", "u8"),
            ])

class GetUseCurrentEnabledResponse(Response):
    enabled: bool

    def __init__(self, enabled: bool = False):
        self.enabled = enabled
        super().__init__(
            5772,
            3,
            [
                Parameter("enabled", "bool"),
            ])

class SetAvailableResponse(Response):
    def __init__(self):
        super().__init__(
            4710,
            6)

class SetDetailedLogEnabledResponse(Response):
    def __init__(self):
        super().__init__(
            5772,
            2)

class SetEnabledResponse(Response):
    def __init__(self):
        super().__init__(
            4710,
            2)

class SetMeanCutCurrentResponse(Response):
    def __init__(self):
        super().__init__(
            5772,
            7)

class SetMeanCutIntensityResponse(Response):
    def __init__(self):
        super().__init__(
            5772,
            8)

class SetSensitivityResponse(Response):
    def __init__(self):
        super().__init__(
            4710,
            4)

class SetUseCurrentEnabledResponse(Response):
    def __init__(self):
        super().__init__(
            5772,
            4)

class StartTriggerResponse(Response):
    def __init__(self):
        super().__init__(
            4710,
            7)

class SubscribeAllEventsResponse(Response):
    def __init__(self):
        super().__init__(
            4710,
            10)

class GetAllStatisticsResponse(Response):
    total_running_time: int
    total_cutting_time: int
    total_charging_time: int
    total_searching_time: int
    number_of_collisions: int
    number_of_charging_cycles: int
    cutting_blade_usage_time: int

    def __init__(self, total_running_time: int = 0, total_cutting_time: int = 0, total_charging_time: int = 0, total_searching_time: int = 0, number_of_collisions: int = 0, number_of_charging_cycles: int = 0, cutting_blade_usage_time: int = 0):
        self.total_running_time = total_running_time
        self.total_cutting_time = total_cutting_time
        self.total_charging_time = total_charging_time
        self.total_searching_time = total_searching_time
        self.number_of_collisions = number_of_collisions
        self.number_of_charging_cycles = number_of_charging_cycles
        self.cutting_blade_usage_time = cutting_blade_usage_time
        super().__init__(
            4726,
            0,
            [
                Parameter("total_running_time", "u32"),
                Parameter("total_cutting_time", "u32"),
                Parameter("total_charging_time", "u32"),
                Parameter("total_searching_time", "u32"),
                Parameter("number_of_collisions", "u32"),
                Parameter("number_of_charging_cycles", "u32"),
                Parameter("cutting_blade_usage_time", "u32"),
            ])

class GetCuttingBladeUsageTimeResponse(Response):
    cutting_blade_usage_time: int

    def __init__(self, cutting_blade_usage_time: int = 0):
        self.cutting_blade_usage_time = cutting_blade_usage_time
        super().__init__(
            4726,
            7,
            [
                Parameter("cutting_blade_usage_time", "u32"),
            ])

class GetNumberOfChargingCyclesResponse(Response):
    number_of_charging_cycles: int

    def __init__(self, number_of_charging_cycles: int = 0):
        self.number_of_charging_cycles = number_of_charging_cycles
        super().__init__(
            4726,
            6,
            [
                Parameter("number_of_charging_cycles", "u32"),
            ])

class GetNumberOfCollisionsResponse(Response):
    number_of_collisions: int

    def __init__(self, number_of_collisions: int = 0):
        self.number_of_collisions = number_of_collisions
        super().__init__(
            4726,
            5,
            [
                Parameter("number_of_collisions", "u32"),
            ])

class GetTotalChargingTimeResponse(Response):
    total_charging_time: int

    def __init__(self, total_charging_time: int = 0):
        self.total_charging_time = total_charging_time
        super().__init__(
            4726,
            3,
            [
                Parameter("total_charging_time", "u32"),
            ])

class GetTotalCuttingTimeResponse(Response):
    total_cutting_time: int

    def __init__(self, total_cutting_time: int = 0):
        self.total_cutting_time = total_cutting_time
        super().__init__(
            4726,
            2,
            [
                Parameter("total_cutting_time", "u32"),
            ])

class GetTotalRunningTimeResponse(Response):
    total_running_time: int

    def __init__(self, total_running_time: int = 0):
        self.total_running_time = total_running_time
        super().__init__(
            4726,
            1,
            [
                Parameter("total_running_time", "u32"),
            ])

class GetTotalSearchingTimeResponse(Response):
    total_searching_time: int

    def __init__(self, total_searching_time: int = 0):
        self.total_searching_time = total_searching_time
        super().__init__(
            4726,
            4,
            [
                Parameter("total_searching_time", "u32"),
            ])

class ResetCuttingBladeUsageTimeResponse(Response):
    def __init__(self):
        super().__init__(
            4726,
            8)

class ClearStartupSequenceRequiredResponse(Response):
    def __init__(self):
        super().__init__(
            4698,
            0)

class GetConfigVersionStringResponse(Response):
    config_version: str

    def __init__(self, config_version: str = ""):
        self.config_version = config_version
        super().__init__(
            4698,
            12,
            [
                Parameter("config_version", "str"),
            ])

class GetLocalHmiAvailableResponse(Response):
    available: bool

    def __init__(self, available: bool = False):
        self.available = available
        super().__init__(
            4698,
            7,
            [
                Parameter("available", "bool"),
            ])

class GetModelResponse(Response):
    device_type: int
    device_variant: int

    def __init__(self, device_type: int = 0, device_variant: int = 0):
        self.device_type = device_type
        self.device_variant = device_variant
        super().__init__(
            4698,
            9,
            [
                Parameter("device_type", "u8"),
                Parameter("device_variant", "u8"),
            ])

class GetSerialNumberResponse(Response):
    serial_number: int

    def __init__(self, serial_number: int = 0):
        self.serial_number = serial_number
        super().__init__(
            4698,
            10,
            [
                Parameter("serial_number", "u32"),
            ])

class GetStartupSequenceRequiredResponse(Response):
    required: bool

    def __init__(self, required: bool = False):
        self.required = required
        super().__init__(
            4698,
            2,
            [
                Parameter("required", "bool"),
            ])

class GetSwPackageVersionStringResponse(Response):
    sw_package_version: str

    def __init__(self, sw_package_version: str = ""):
        self.sw_package_version = sw_package_version
        super().__init__(
            4698,
            22,
            [
                Parameter("sw_package_version", "str"),
            ])

class GetUserMowerNameAsAsciiStringResponse(Response):
    name: str

    def __init__(self, name: str = ""):
        self.name = name
        super().__init__(
            4698,
            5,
            [
                Parameter("name", "str"),
            ])

class GetUserMowerNameResponse(Response):
    name: bytes

    def __init__(self, name: bytes = bytes()):
        self.name = name
        super().__init__(
            4698,
            3,
            [
                Parameter("name", "bytes"),
            ])

class ResetToUserDefaultResponse(Response):
    def __init__(self):
        super().__init__(
            4698,
            8)

class SetStartupSequenceRequiredResponse(Response):
    def __init__(self):
        super().__init__(
            4698,
            1)

class SetUserMowerNameAsAsciiStringResponse(Response):
    def __init__(self):
        super().__init__(
            4698,
            6)

class SetUserMowerNameResponse(Response):
    def __init__(self):
        super().__init__(
            4698,
            4)

class EnableEventsResponse(Response):
    def __init__(self):
        super().__init__(
            4674,
            0)

class GetPowerModeResponse(Response):
    mode: int

    def __init__(self, mode: int = 0):
        self.mode = mode
        super().__init__(
            4674,
            1,
            [
                Parameter("mode", "u8"),
            ])

class KeepAliveResponse(Response):
    def __init__(self):
        super().__init__(
            4674,
            2)

class GetMaxGardenAreaResponse(Response):
    square_meters: int

    def __init__(self, square_meters: int = 0):
        self.square_meters = square_meters
        super().__init__(
            2,
            30,
            [
                Parameter("square_meters", "u16"),
            ])

class SetLoopDetectionResponse(Response):
    loop_detection: int

    def __init__(self, loop_detection: int = 0):
        self.loop_detection = loop_detection
        super().__init__(
            2,
            136,
            [
                Parameter("loop_detection", "u8"),
            ])

class ConnectResponse(Response):
    new_link_id: int

    def __init__(self, new_link_id: int = 0):
        self.new_link_id = new_link_id
        super().__init__(
            21,
            None,
            [
                Parameter("new_link_id", "u32"),
            ])

class ConnectToNodeResponse(Response):
    def __init__(self):
        super().__init__(
            97,
            0)

class CreateLinkResponse(Response):
    def __init__(self):
        super().__init__(
            97,
            0)

class DeleteLinkResponse(Response):
    def __init__(self):
        super().__init__(
            97,
            0)

class DiscoverResponse(Response):
    response_id: int
    traceback_id: int
    node_type: int
    node_name: str

    def __init__(self, response_id: int = 0, traceback_id: int = 0, node_type: int = 0, node_name: str = ""):
        self.response_id = response_id
        self.traceback_id = traceback_id
        self.node_type = node_type
        self.node_name = node_name
        super().__init__(
            19,
            None,
            [
               Parameter("response_id", "u8"),
               Parameter("traceback_id", "u32"),
               Parameter("node_type", "u32"),
               Parameter("node_name", "str"),
            ])

class GetNodeNameResponse(Response):
    node_name: str

    def __init__(self, node_name: str = ""):
        self.node_name = node_name
        super().__init__(
            97,
            0,
            [
                Parameter("node_name", "str"),
            ])

class GetNodeTypeResponse(Response):
    node_type: int

    def __init__(self, node_type: int = 0):
        self.node_type = node_type
        super().__init__(
            97,
            0,
            [
                Parameter("node_type", "u32"),
            ])

class GetVersionStringResponse(Response):
    get_version_string: str

    def __init__(self, get_version_string: str = ""):
        self.get_version_string = get_version_string
        super().__init__(
            97,
            0,
            [
                Parameter("get_version_string", "str"),
            ])

class IsPacketTypeSupportedResponse(Response):
    is_supported: bool

    def __init__(self, is_supported: bool = False):
        self.is_supported = is_supported
        super().__init__(
            97,
            0,
            [
                Parameter("is_supported", "bool"),
            ])

class IsProtocolSupportedResponse(Response):
    is_supported: bool

    def __init__(self, is_supported: bool = False):
        self.is_supported = is_supported
        super().__init__(
            97,
            0,
            [
                Parameter("is_supported", "bool"),
            ])

class ListAllNodesResponse(Response):
    def __init__(self):
        super().__init__(
            97,
            0)

class RouteRawResponse(Response):
    def __init__(self):
        super().__init__(
            97,
            0)

class RouteResponse(Response):
    def __init__(self):
        super().__init__(
            97,
            0)

class SendDummyDataResponse(Response):
    def __init__(self):
        super().__init__(
            97,
            0)

class SetProtocolVersionResponse(Response):
    protocol: int
    unknown: int

    def __init__(self, protocol: int = 0, unknown: int = 0):
        self.protocol = protocol
        self.unknown = unknown
        super().__init__(
            9,
            None,
            [
                Parameter("protocol", "u8"),
                Parameter("unknown", "u8"),
            ])

class UnrouteResponse(Response):
    def __init__(self):
        super().__init__(
            97,
            0)

class ChallengeResponseV2Request(Request):
    challenge_response: bytes

    def __init__(self, challenge_response: bytes = bytes()):
        self.challenge_response = challenge_response
        super().__init__(
            4664,
            11, ChallengeResponseV2Response,
            [
                Parameter("challenge_response", "bytes"),
            ])

class EnterOperatorPinRequest(Request):
    pin: int

    def __init__(self, pin: int = 0):
        self.pin = pin
        super().__init__(
            4664,
            4, EnterOperatorPinResponse,
            [
                Parameter("pin", "u16"),
            ])

class GetBlockedTimeRequest(Request):
    def __init__(self):
        super().__init__(
            4664,
            2, GetBlockedTimeResponse)

class GetLoginLevelRequest(Request):
    def __init__(self):
        super().__init__(
            4664,
            0, GetLoginLevelResponse)

class GetRemainingLoginAttemptsRequest(Request):
    def __init__(self):
        super().__init__(
            5124,
            10, GetRemainingLoginAttemptsResponse)

class GetSecurityCodeV2Request(Request):
    def __init__(self):
        super().__init__(
            4664,
            14, GetSecurityCodeV2Response)

class InitiateAuthenticationV2Request(Request):
    login_level: int

    def __init__(self, login_level: int = 0):
        self.login_level = login_level
        super().__init__(
            4664,
            10, InitiateAuthenticationV2Response,
            [
                Parameter("login_level", "u8"),
            ])

class IsBlockedRequest(Request):
    def __init__(self):
        super().__init__(
            4664,
            1, IsBlockedResponse)

class IsOperatorLoggedInRequest(Request):
    def __init__(self):
        super().__init__(
            4664,
            3, IsOperatorLoggedInResponse)

class IsTrustedToEnterSafetyPinRequest(Request):
    def __init__(self):
        super().__init__(
            4664,
            8, IsTrustedToEnterSafetyPinResponse)

class LogoutRequest(Request):
    def __init__(self):
        super().__init__(
            4664,
            15, LogoutResponse)

class SetOperatorPinRequest(Request):
    old_pin: int
    new_pin: int

    def __init__(self, old_pin: int = 0, new_pin: int = 0):
        self.old_pin = old_pin
        self.new_pin = new_pin
        super().__init__(
            4664,
            5, SetOperatorPinResponse,
            [
                Parameter("old_pin", "u16"),
                Parameter("new_pin", "u16"),
            ])

class SubscribeAllEventsRequest(Request):
    def __init__(self):
        super().__init__(
            4664,
            17, SubscribeAllEventsResponse)

class GetAllSettingsRequest(Request):
    def __init__(self):
        super().__init__(
            4460,
            8, GetAllSettingsResponse)

class GetAvailableRequest(Request):
    def __init__(self):
        super().__init__(
            4460,
            2, GetAvailableResponse)

class GetEnabledRequest(Request):
    def __init__(self):
        super().__init__(
            4460,
            4, GetEnabledResponse)

class GetRestrictionReasonRequest(Request):
    def __init__(self):
        super().__init__(
            4460,
            9, GetRestrictionReasonResponse)

class GetSensitivityRequest(Request):
    def __init__(self):
        super().__init__(
            4460,
            6, GetSensitivityResponse)

class IsReadyRequest(Request):
    def __init__(self):
        super().__init__(
            4460,
            10, IsReadyResponse)

class SetAvailableRequest(Request):
    available: bool

    def __init__(self, available: bool = False):
        self.available = available
        super().__init__(
            4460,
            3, SetAvailableResponse,
            [
                Parameter("available", "bool"),
            ])

class SetEnabledRequest(Request):
    enabled: bool

    def __init__(self, enabled: bool = False):
        self.enabled = enabled
        super().__init__(
            4460,
            5, SetEnabledResponse,
            [
                Parameter("enabled", "bool"),
            ])

class SetSensitivityRequest(Request):
    sensitivity: int

    def __init__(self, sensitivity: int = 0):
        self.sensitivity = sensitivity
        super().__init__(
            4460,
            7, SetSensitivityResponse,
            [
                Parameter("sensitivity", "u8"),
            ])

class SubscribeAllEventsRequest(Request):
    def __init__(self):
        super().__init__(
            4460,
            0, SubscribeAllEventsResponse)

class SubscribeEventChannelRequest(Request):
    event_channel: int

    def __init__(self, event_channel: int = 0):
        self.event_channel = event_channel
        super().__init__(
            4460,
            1, SubscribeEventChannelResponse,
            [
                Parameter("event_channel", "u8"),
            ])

class GetBatteryLevelRequest(Request):
    def __init__(self):
        super().__init__(
            4106,
            20, GetBatteryLevelResponse)

class GetCapacityRequest(Request):
    index: int

    def __init__(self, index: int = 0):
        self.index = index
        super().__init__(
            4106,
            0, GetCapacityResponse,
            [
                Parameter("index", "u8"),
            ])

class GetEnergyLevelRequest(Request):
    index: int

    def __init__(self, index: int = 0):
        self.index = index
        super().__init__(
            4106,
            1, GetEnergyLevelResponse,
            [
                Parameter("index", "u8"),
            ])

class GetRemainingChargingTimeRequest(Request):
    def __init__(self):
        super().__init__(
            4106,
            22, GetRemainingChargingTimeResponse)

class GetSimulatedEnergyLevelRequest(Request):
    index: int

    def __init__(self, index: int = 0):
        self.index = index
        super().__init__(
            4106,
            3, GetSimulatedEnergyLevelResponse,
            [
                Parameter("index", "u8"),
            ])

class GetSimulationRequest(Request):
    index: int

    def __init__(self, index: int = 0):
        self.index = index
        super().__init__(
            4106,
            5, GetSimulationResponse,
            [
                Parameter("index", "u8"),
            ])

class IsChargingRequest(Request):
    def __init__(self):
        super().__init__(
            4106,
            21, IsChargingResponse)

class SetSimulatedEnergyLevelRequest(Request):
    index: int
    energy_level: int

    def __init__(self, index: int = 0, energy_level: int = 0):
        self.index = index
        self.energy_level = energy_level
        super().__init__(
            4106,
            2, SetSimulatedEnergyLevelResponse,
            [
                Parameter("index", "u8"),
                Parameter("energy_level", "s16"),
            ])

class SetSimulationRequest(Request):
    index: int
    on_off: bool

    def __init__(self, index: int = 0, on_off: bool = False):
        self.index = index
        self.on_off = on_off
        super().__init__(
            4106,
            4, SetSimulationResponse,
            [
                Parameter("index", "u8"),
                Parameter("on_off", "bool"),
            ])

class DisablePairableRequest(Request):
    def __init__(self):
        super().__init__(
            4678,
            7, DisablePairableResponse)

class ErasePairedDeviceListRequest(Request):
    def __init__(self):
        super().__init__(
            4678,
            3, ErasePairedDeviceListResponse)

class GetAdvertisingRequest(Request):
    def __init__(self):
        super().__init__(
            4678,
            9, GetAdvertisingResponse)

class GetConnectedRequest(Request):
    def __init__(self):
        super().__init__(
            4678,
            2, GetConnectedResponse)

class GetPairableRequest(Request):
    def __init__(self):
        super().__init__(
            4678,
            1, GetPairableResponse)

class SetAdvertisingRequest(Request):
    value: bool

    def __init__(self, value: bool = False):
        self.value = value
        super().__init__(
            4678,
            8, SetAdvertisingResponse,
            [
                Parameter("value", "bool"),
            ])

class SetPairableRequest(Request):
    timeout: int

    def __init__(self, timeout: int = 0):
        self.timeout = timeout
        super().__init__(
            4678,
            0, SetPairableResponse,
            [
                Parameter("timeout", "u32"),
            ])

class SubscribeAllEventsRequest(Request):
    def __init__(self):
        super().__init__(
            4678,
            10, SubscribeAllEventsResponse)

class AddTaskRequest(Request):
    start: int
    duration: int
    use_on_monday: bool
    use_on_tuesday: bool
    use_on_wednesday: bool
    use_on_thursday: bool
    use_on_friday: bool
    use_on_saturday: bool
    use_on_sunday: bool

    def __init__(self, start: int = 0, duration: int = 0, use_on_monday: bool = False, use_on_tuesday: bool = False, use_on_wednesday: bool = False, use_on_thursday: bool = False, use_on_friday: bool = False, use_on_saturday: bool = False, use_on_sunday: bool = False):
        self.start = start
        self.duration = duration
        self.use_on_monday = use_on_monday
        self.use_on_tuesday = use_on_tuesday
        self.use_on_wednesday = use_on_wednesday
        self.use_on_thursday = use_on_thursday
        self.use_on_friday = use_on_friday
        self.use_on_saturday = use_on_saturday
        self.use_on_sunday = use_on_sunday
        super().__init__(
            4690,
            7, AddTaskResponse,
            [
                Parameter("start", "u32"),
                Parameter("duration", "u32"),
                Parameter("use_on_monday", "bool"),
                Parameter("use_on_tuesday", "bool"),
                Parameter("use_on_wednesday", "bool"),
                Parameter("use_on_thursday", "bool"),
                Parameter("use_on_friday", "bool"),
                Parameter("use_on_saturday", "bool"),
                Parameter("use_on_sunday", "bool"),
            ])

class CommitTaskTransactionRequest(Request):
    def __init__(self):
        super().__init__(
            4690,
            11, CommitTaskTransactionResponse)

class DeleteAllTasksRequest(Request):
    def __init__(self):
        super().__init__(
            4690,
            9, DeleteAllTasksResponse)

class DeleteTaskRequest(Request):
    index: int

    def __init__(self, index: int = 0):
        self.index = index
        super().__init__(
            4690,
            8, DeleteTaskResponse,
            [
                Parameter("index", "u32"),
            ])

class GetNumberOfTasksRequest(Request):
    def __init__(self):
        super().__init__(
            4690,
            4, GetNumberOfTasksResponse)

class GetTaskRequest(Request):
    index: int

    def __init__(self, index: int = 0):
        self.index = index
        super().__init__(
            4690,
            5, GetTaskResponse,
            [
                Parameter("index", "u32"),
            ])

class GetTimeRequest(Request):
    def __init__(self):
        super().__init__(
            4690,
            2, GetTimeResponse)

class param1Boolean6():
    index: int
    start: int
    duration: int
    use_on_monday: bool
    use_on_tuesday: bool
    use_on_wednesday: bool
    use_on_thursday: bool
    use_on_friday: bool
    use_on_saturday: bool
    use_on_sunday: bool

    def __init__(self, index: int = 0, start: int = 0, duration: int = 0, use_on_monday: bool = False, use_on_tuesday: bool = False, use_on_wednesday: bool = False, use_on_thursday: bool = False, use_on_friday: bool = False, use_on_saturday: bool = False, use_on_sunday: bool = False):
        self.index = index
        self.start = start
        self.duration = duration
        self.use_on_monday = use_on_monday
        self.use_on_tuesday = use_on_tuesday
        self.use_on_wednesday = use_on_wednesday
        self.use_on_thursday = use_on_thursday
        self.use_on_friday = use_on_friday
        self.use_on_saturday = use_on_saturday
        self.use_on_sunday = use_on_sunday
        super().__init__(
            4690,
            6, SetTaskResponse,
            [
                Parameter("index", "u32"),
                Parameter("start", "u32"),
                Parameter("duration", "u32"),
                Parameter("use_on_monday", "bool"),
                Parameter("use_on_tuesday", "bool"),
                Parameter("use_on_wednesday", "bool"),
                Parameter("use_on_thursday", "bool"),
                Parameter("use_on_friday", "bool"),
                Parameter("use_on_saturday", "bool"),
                Parameter("use_on_sunday", "bool"),
            ])

class SetTimeRequest(Request):
    time: int

    def __init__(self, time: int = 0):
        self.time = time
        super().__init__(
            4690,
            3, SetTimeResponse,
            [
                Parameter("time", "u32"),
            ])

class StartTaskTransactionRequest(Request):
    def __init__(self):
        super().__init__(
            4690,
            10, StartTaskTransactionResponse)

class SubscribeAllEventsRequest(Request):
    def __init__(self):
        super().__init__(
            4690,
            0, SubscribeAllEventsResponse)

class SubscribeEventChannelRequest(Request):
    event_channel: int

    def __init__(self, event_channel: int = 0):
        self.event_channel = event_channel
        super().__init__(
            4690,
            1, SubscribeEventChannelResponse,
            [
                Parameter("event_channel", "u8"),
            ])

class ChargingGateOffRequest(Request):
    gate_index: int

    def __init__(self, gate_index: int = 0):
        self.gate_index = gate_index
        super().__init__(
            4486,
            1, ChargingGateOffResponse,
            [
                Parameter("gate_index", "u8"),
            ])

class ChargingGateOnRequest(Request):
    gate_index: int

    def __init__(self, gate_index: int = 0):
        self.gate_index = gate_index
        super().__init__(
            4486,
            2, ChargingGateOnResponse,
            [
                Parameter("gate_index", "u8"),
            ])

class ChargingOffRequest(Request):
    def __init__(self):
        super().__init__(
            4486,
            0, ChargingOffResponse)

class GetChargingErrorCountRequest(Request):
    index: int

    def __init__(self, index: int = 0):
        self.index = index
        super().__init__(
            5512,
            24, GetChargingErrorCountResponse,
            [
                Parameter("index", "u8"),
            ])

class GetChargingPowerDetectedCountRequest(Request):
    def __init__(self):
        super().__init__(
            5512,
            21, GetChargingPowerDetectedCountResponse)

class GetCurrentChargingTimeMaxRequest(Request):
    def __init__(self):
        super().__init__(
            5512,
            19, GetCurrentChargingTimeMaxResponse)

class GetCurrentChargingTimeRequest(Request):
    index: int

    def __init__(self, index: int = 0):
        self.index = index
        super().__init__(
            5512,
            15, GetCurrentChargingTimeResponse,
            [
                Parameter("index", "u8"),
            ])

class GetIsBatteryChargingPreventedRequest(Request):
    index: int

    def __init__(self, index: int = 0):
        self.index = index
        super().__init__(
            5512,
            10, GetIsBatteryChargingPreventedResponse,
            [
                Parameter("index", "u8"),
            ])

class GetIsBatteryChargingRequest(Request):
    index: int

    def __init__(self, index: int = 0):
        self.index = index
        super().__init__(
            5512,
            8, GetIsBatteryChargingResponse,
            [
                Parameter("index", "u8"),
            ])

class GetIsChargingPowerDetectedRequest(Request):
    def __init__(self):
        super().__init__(
            5512,
            7, GetIsChargingPowerDetectedResponse)

class GetIsChargingPreventedRequest(Request):
    def __init__(self):
        super().__init__(
            5512,
            11, GetIsChargingPreventedResponse)

class GetIsChargingRequest(Request):
    def __init__(self):
        super().__init__(
            5512,
            9, GetIsChargingResponse)

class GetIsInChargingStateRequest(Request):
    index: int

    def __init__(self, index: int = 0):
        self.index = index
        super().__init__(
            5512,
            14, GetIsInChargingStateResponse,
            [
                Parameter("index", "u8"),
            ])

class GetLastChargingTimeMaxRequest(Request):
    def __init__(self):
        super().__init__(
            5512,
            20, GetLastChargingTimeMaxResponse)

class GetLastChargingTimeRequest(Request):
    index: int

    def __init__(self, index: int = 0):
        self.index = index
        super().__init__(
            5512,
            18, GetLastChargingTimeResponse,
            [
                Parameter("index", "u8"),
            ])

class GetRemainingChargingTimeRequest(Request):
    index: int

    def __init__(self, index: int = 0):
        self.index = index
        super().__init__(
            5512,
            16, GetRemainingChargingTimeResponse,
            [
                Parameter("index", "u8"),
            ])

class GetRemainingTotalChargingTimeRequest(Request):
    def __init__(self):
        super().__init__(
            5512,
            17, GetRemainingTotalChargingTimeResponse)

class GetSimChargingGateRequest(Request):
    index: int

    def __init__(self, index: int = 0):
        self.index = index
        super().__init__(
            5512,
            2, GetSimChargingGateResponse,
            [
                Parameter("index", "u8"),
            ])

class GetSimExtPowerDetectedRequest(Request):
    def __init__(self):
        super().__init__(
            5512,
            4, GetSimExtPowerDetectedResponse)

class GetSimIsChargingEnabledRequest(Request):
    def __init__(self):
        super().__init__(
            5744,
            5, GetSimIsChargingEnabledResponse)

class GetSimIsPowerConnectedRequest(Request):
    def __init__(self):
        super().__init__(
            5744,
            3, GetSimIsPowerConnectedResponse)

class GetSimulationRequest(Request):
    def __init__(self):
        super().__init__(
            5512,
            1, GetSimulationResponse)

class GetStateRequest(Request):
    index: int

    def __init__(self, index: int = 0):
        self.index = index
        super().__init__(
            5512,
            12, GetStateResponse,
            [
                Parameter("index", "u8"),
            ])

class GetStatusRequest(Request):
    def __init__(self):
        super().__init__(
            4486,
            8, GetStatusResponse)

class GetSubStateRequest(Request):
    index: int
    state: int

    def __init__(self, index: int = 0, state: int = 0):
        self.index = index
        self.state = state
        super().__init__(
            5512,
            13, GetSubStateResponse,
            [
                Parameter("index", "u8"),
                Parameter("state", "u8"),
            ])

class InjectChargingErrorRequest(Request):
    index: int

    def __init__(self, index: int = 0):
        self.index = index
        super().__init__(
            5512,
            6, InjectChargingErrorResponse,
            [
                Parameter("index", "u8"),
            ])

class IsChargingEnabledRequest(Request):
    def __init__(self):
        super().__init__(
            4486,
            3, IsChargingEnabledResponse)

class IsChargingPowerConnectedRequest(Request):
    def __init__(self):
        super().__init__(
            4486,
            4, IsChargingPowerConnectedResponse)

class IsChargingPrevetnedRequest(Request):
    def __init__(self):
        super().__init__(
            4486,
            6, IsChargingPrevetnedResponse)

class IsReadyRequest(Request):
    def __init__(self):
        super().__init__(
            4486,
            9, IsReadyResponse)

class PreventChargingRequest(Request):
    def __init__(self):
        super().__init__(
            4486,
            5, PreventChargingResponse)

class PreventSingleChargingRequest(Request):
    index: int

    def __init__(self, index: int = 0):
        self.index = index
        super().__init__(
            5512,
            22, PreventSingleChargingResponse,
            [
                Parameter("index", "u8"),
            ])

class ResetStatusRequest(Request):
    def __init__(self):
        super().__init__(
            5512,
            23, ResetStatusResponse)

class SetSimChargingGateRequest(Request):
    index: int
    enabled: bool

    def __init__(self, index: int = 0, enabled: bool = False):
        self.index = index
        self.enabled = enabled
        super().__init__(
            5512,
            3, SetSimChargingGateResponse,
            [
                Parameter("index", "u8"),
                Parameter("enabled", "bool"),
            ])

class SetSimExtPowerDetectedRequest(Request):
    detected: bool

    def __init__(self, detected: bool = False):
        self.detected = detected
        super().__init__(
            5512,
            5, SetSimExtPowerDetectedResponse,
            [
                Parameter("detected", "bool"),
            ])

class SetSimIsChargingEnabledRequest(Request):
    sim_is_charging_enabled: bool

    def __init__(self, sim_is_charging_enabled: bool = False):
        self.sim_is_charging_enabled = sim_is_charging_enabled
        super().__init__(
            5744,
            4, SetSimIsChargingEnabledResponse,
            [
                Parameter("sim_is_charging_enabled", "bool"),
            ])

class SetSimIsPowerConnectedRequest(Request):
    sim_is_power_connected: bool

    def __init__(self, sim_is_power_connected: bool = False):
        self.sim_is_power_connected = sim_is_power_connected
        super().__init__(
            5744,
            2, SetSimIsPowerConnectedResponse,
            [
                Parameter("sim_is_power_connected", "bool"),
            ])

class SetSimulationRequest(Request):
    sim_on: bool

    def __init__(self, sim_on: bool = False):
        self.sim_on = sim_on
        super().__init__(
            5512,
            0, SetSimulationResponse,
            [
                Parameter("sim_on", "bool"),
            ])

class SubscribeAllEventsRequest(Request):
    def __init__(self):
        super().__init__(
            4486,
            7, SubscribeAllEventsResponse)

class GetAllSettingsRequest(Request):
    def __init__(self):
        super().__init__(
            4692,
            10, GetAllSettingsResponse)

class GetEcoModeEnabledRequest(Request):
    def __init__(self):
        super().__init__(
            4692,
            6, GetEcoModeEnabledResponse)

class GetMowerHouseInstalledRequest(Request):
    def __init__(self):
        super().__init__(
            4692,
            4, GetMowerHouseInstalledResponse)

class InitiateNewPairingRequest(Request):
    def __init__(self):
        super().__init__(
            4692,
            2, InitiateNewPairingResponse)

class SetEcoModeEnabledRequest(Request):
    eco_mode_enabled: bool

    def __init__(self, eco_mode_enabled: bool = False):
        self.eco_mode_enabled = eco_mode_enabled
        super().__init__(
            4692,
            5, SetEcoModeEnabledResponse,
            [
                Parameter("eco_mode_enabled", "bool"),
            ])

class SetMowerHouseInstalledRequest(Request):
    mower_house_installed: bool

    def __init__(self, mower_house_installed: bool = False):
        self.mower_house_installed = mower_house_installed
        super().__init__(
            4692,
            3, SetMowerHouseInstalledResponse,
            [
                Parameter("mower_house_installed", "bool"),
            ])

class SubscribeAllEventsRequest(Request):
    def __init__(self):
        super().__init__(
            4692,
            11, SubscribeAllEventsResponse)

class SubscribeEventChannelRequest(Request):
    event_channel: int

    def __init__(self, event_channel: int = 0):
        self.event_channel = event_channel
        super().__init__(
            4692,
            12, SubscribeEventChannelResponse,
            [
                Parameter("event_channel", "u8"),
            ])

class GetAllSettingsRequest(Request):
    def __init__(self):
        super().__init__(
            4712,
            2, GetAllSettingsResponse)

class GetDrivePastWireRequest(Request):
    def __init__(self):
        super().__init__(
            4712,
            0, GetDrivePastWireResponse)

class SetDrivePastWireRequest(Request):
    distance: int

    def __init__(self, distance: int = 0):
        self.distance = distance
        super().__init__(
            4712,
            1, SetDrivePastWireResponse,
            [
                Parameter("distance", "u16"),
            ])

class SubscribeAllEventsRequest(Request):
    def __init__(self):
        super().__init__(
            4712,
            9, SubscribeAllEventsResponse)

class GetBoundaryCorridorRequest(Request):
    def __init__(self):
        super().__init__(
            4706,
            24, GetBoundaryCorridorResponse)

class GetCurrentDistanceRequest(Request):
    def __init__(self):
        super().__init__(
            4706,
            16, GetCurrentDistanceResponse)

class GetNumberOfGuidesRequest(Request):
    def __init__(self):
        super().__init__(
            4706,
            14, GetNumberOfGuidesResponse)

class GetPassageCuttingEnabledRequest(Request):
    id: int

    def __init__(self, id: int = 0):
        self.id = id
        super().__init__(
            4706,
            26, GetPassageCuttingEnabledResponse,
            [
                Parameter("id", "u8"),
            ])

class GetStartingPointDistanceRequest(Request):
    id: int

    def __init__(self, id: int = 0):
        self.id = id
        super().__init__(
            4706,
            10, GetStartingPointDistanceResponse,
            [
                Parameter("id", "u8"),
            ])

class GetStartingPointEnabledRequest(Request):
    id: int

    def __init__(self, id: int = 0):
        self.id = id
        super().__init__(
            4706,
            6, GetStartingPointEnabledResponse,
            [
                Parameter("id", "u8"),
            ])

class GetStartingPointMaxRequest(Request):
    def __init__(self):
        super().__init__(
            4706,
            28, GetStartingPointMaxResponse)

class GetStartingPointProportionRequest(Request):
    id: int

    def __init__(self, id: int = 0):
        self.id = id
        super().__init__(
            4706,
            12, GetStartingPointProportionResponse,
            [
                Parameter("id", "u8"),
            ])

class GetStartingPointSettingsRequest(Request):
    id: int

    def __init__(self, id: int = 0):
        self.id = id
        super().__init__(
            4706,
            21, GetStartingPointSettingsResponse,
            [
                Parameter("id", "u8"),
            ])

class GetStartingPointWireRequest(Request):
    id: int

    def __init__(self, id: int = 0):
        self.id = id
        super().__init__(
            4706,
            8, GetStartingPointWireResponse,
            [
                Parameter("id", "u8"),
            ])

class GetTestErrorRequest(Request):
    def __init__(self):
        super().__init__(
            4706,
            29, GetTestErrorResponse)

class GetTestModeRequest(Request):
    def __init__(self):
        super().__init__(
            4706,
            22, GetTestModeResponse)

class GetTestStateRequest(Request):
    def __init__(self):
        super().__init__(
            4706,
            23, GetTestStateResponse)

class SetBoundaryCorridorRequest(Request):
    max: int

    def __init__(self, max: int = 0):
        self.max = max
        super().__init__(
            4706,
            25, SetBoundaryCorridorResponse,
            [
                Parameter("max", "u8"),
            ])

class SetPassageCuttingEnabledRequest(Request):
    id: int
    passage_cutting_enabled: bool

    def __init__(self, id: int = 0, passage_cutting_enabled: bool = False):
        self.id = id
        self.passage_cutting_enabled = passage_cutting_enabled
        super().__init__(
            4706,
            27, SetPassageCuttingEnabledResponse,
            [
                Parameter("id", "u8"),
                Parameter("passage_cutting_enabled", "bool"),
            ])

class SetStartingPointDistanceRequest(Request):
    id: int
    distance: int

    def __init__(self, id: int = 0, distance: int = 0):
        self.id = id
        self.distance = distance
        super().__init__(
            4706,
            11, SetStartingPointDistanceResponse,
            [
                Parameter("id", "u8"),
                Parameter("distance", "u16"),
            ])

class SetStartingPointEnabledRequest(Request):
    id: int
    enabled: bool

    def __init__(self, id: int = 0, enabled: bool = False):
        self.id = id
        self.enabled = enabled
        super().__init__(
            4706,
            7, SetStartingPointEnabledResponse,
            [
                Parameter("id", "u8"),
                Parameter("enabled", "bool"),
            ])

class SetStartingPointProportionRequest(Request):
    id: int
    proportion: int

    def __init__(self, id: int = 0, proportion: int = 0):
        self.id = id
        self.proportion = proportion
        super().__init__(
            4706,
            13, SetStartingPointProportionResponse,
            [
                Parameter("id", "u8"),
                Parameter("proportion", "u8"),
            ])

class SetStartingPointWireRequest(Request):
    id: int
    wire: int

    def __init__(self, id: int = 0, wire: int = 0):
        self.id = id
        self.wire = wire
        super().__init__(
            4706,
            9, SetStartingPointWireResponse,
            [
                Parameter("id", "u8"),
                Parameter("wire", "u8"),
            ])

class SubscribeAllEventsRequest(Request):
    def __init__(self):
        super().__init__(
            4706,
            19, SubscribeAllEventsResponse)

class SubscribeEventChannelRequest(Request):
    event_channel: int

    def __init__(self, event_channel: int = 0):
        self.event_channel = event_channel
        super().__init__(
            4706,
            20, SubscribeEventChannelResponse,
            [
                Parameter("event_channel", "u8"),
            ])

class TestAbortRequest(Request):
    def __init__(self):
        super().__init__(
            4706,
            18, TestAbortResponse)

class TestFollowInRequest(Request):
    wire: int

    def __init__(self, wire: int = 0):
        self.wire = wire
        super().__init__(
            4706,
            17, TestFollowInResponse,
            [
                Parameter("wire", "u8"),
            ])

class TestStartingPointRequest(Request):
    id: int
    corridor: int

    def __init__(self, id: int = 0, corridor: int = 0):
        self.id = id
        self.corridor = corridor
        super().__init__(
            4706,
            15, TestStartingPointResponse,
            [
                Parameter("id", "u8"),
                Parameter("corridor", "u8"),
            ])

class GetAllSettingsRequest(Request):
    def __init__(self):
        super().__init__(
            5370,
            8, GetAllSettingsResponse)

class GetAvailableRequest(Request):
    def __init__(self):
        super().__init__(
            5370,
            0, GetAvailableResponse)

class GetEnabledRequest(Request):
    def __init__(self):
        super().__init__(
            5412,
            1, GetEnabledResponse)

class GetEnabledRequestOBP():
    def __init__(self):
        super().__init__(
            5370, 1, GetEnabledResponseOBP)

class SetEnabledRequest(Request):
    enabled: bool

    def __init__(self, enabled: bool = False):
        self.enabled = enabled
        super().__init__(
            5412,
            2, SetEnabledResponse,
            [
                Parameter("enabled", "bool"),
            ])


class SetEnabledRequestOBP():
    enabled: bool

    def __init__(self, enabled: bool = False):
        self.enabled = enabled
        super().__init__(
            5370,
            2, SetEnabledResponseOBP,
            [
                Parameter("enabled", "bool"),
            ])

class SubscribeAllEventsRequest(Request):
    def __init__(self):
        super().__init__(
            5370,
            9, SubscribeAllEventsResponse)

class ClearSettingsRequest(Request):
    def __init__(self):
        super().__init__(
            4462,
            18, ClearSettingsResponse)

class GetCloseToBoundaryLimitRequest(Request):
    def __init__(self):
        super().__init__(
            4462,
            5, GetCloseToBoundaryLimitResponse)

class GetCloseToBoundaryOffsetRequest(Request):
    def __init__(self):
        super().__init__(
            4462,
            6, GetCloseToBoundaryOffsetResponse)

class GetCloseToBoundaryRequest(Request):
    def __init__(self):
        super().__init__(
            4290,
            1, GetCloseToBoundaryResponse)

class GetCloseToCsLimitRequest(Request):
    def __init__(self):
        super().__init__(
            4462,
            30, GetCloseToCsLimitResponse)

class GetCloseToCsOffsetRequest(Request):
    def __init__(self):
        super().__init__(
            4462,
            31, GetCloseToCsOffsetResponse)

class GetCloseToCsRequest(Request):
    def __init__(self):
        super().__init__(
            4290,
            0, GetCloseToCsResponse)

class GetInstalledLoopsRequest(Request):
    def __init__(self):
        super().__init__(
            4462,
            29, GetInstalledLoopsResponse)

class GetLoopSideRequest(Request):
    index: int
    loop: int

    def __init__(self, index: int = 0, loop: int = 0):
        self.index = index
        self.loop = loop
        super().__init__(
            4462,
            33, GetLoopSideResponse,
            [
                Parameter("index", "u8"),
                Parameter("loop", "u8"),
            ])

class GetLoopSignalRequest(Request):
    index: int
    loop: int

    def __init__(self, index: int = 0, loop: int = 0):
        self.index = index
        self.loop = loop
        super().__init__(
            4462,
            12, GetLoopSignalResponse,
            [
                Parameter("index", "u8"),
                Parameter("loop", "u8"),
            ])

class GetLoopSignalsRequest(Request):
    index: int

    def __init__(self, index: int = 0):
        self.index = index
        super().__init__(
            4462,
            13, GetLoopSignalsResponse,
            [
                Parameter("index", "u8"),
            ])

class GetMinMaxRequest(Request):
    def __init__(self):
        super().__init__(
            4462,
            8, GetMinMaxResponse)

class GetNbrAvailableGuidesRequest(Request):
    def __init__(self):
        super().__init__(
            4462,
            22, GetNbrAvailableGuidesResponse)

class GetNoLoopStatusRequest(Request):
    def __init__(self):
        super().__init__(
            4462,
            4, GetNoLoopStatusResponse)

class GetNumSensorsRequest(Request):
    def __init__(self):
        super().__init__(
            4462,
            11, GetNumSensorsResponse)

class GetOnCsStatusRequest(Request):
    def __init__(self):
        super().__init__(
            4462,
            3, GetOnCsStatusResponse)

class GetOutsideStatusRequest(Request):
    def __init__(self):
        super().__init__(
            4462,
            2, GetOutsideStatusResponse)

class GetPeakUpdateActiveRequest(Request):
    def __init__(self):
        super().__init__(
            4462,
            16, GetPeakUpdateActiveResponse)

class GetPeriodTimeRequest(Request):
    def __init__(self):
        super().__init__(
            4462,
            9, GetPeriodTimeResponse)

class GetRawLoopSignalRequest(Request):
    index: int
    loop: int

    def __init__(self, index: int = 0, loop: int = 0):
        self.index = index
        self.loop = loop
        super().__init__(
            4462,
            24, GetRawLoopSignalResponse,
            [
                Parameter("index", "u8"),
                Parameter("loop", "u8"),
            ])

class GetRawLoopSignalsRequest(Request):
    index: int

    def __init__(self, index: int = 0):
        self.index = index
        super().__init__(
            4462,
            25, GetRawLoopSignalsResponse,
            [
                Parameter("index", "u8"),
            ])

class GetSignalQualityRequest(Request):
    index: int

    def __init__(self, index: int = 0):
        self.index = index
        super().__init__(
            4462,
            14, GetSignalQualityResponse,
            [
                Parameter("index", "u8"),
            ])

class GetSyncSensitivityRequest(Request):
    def __init__(self):
        super().__init__(
            4462,
            26, GetSyncSensitivityResponse)

class GetTemporaryPeriodTimeRequest(Request):
    def __init__(self):
        super().__init__(
            4462,
            20, GetTemporaryPeriodTimeResponse)

class IsOnCsRequest(Request):
    mask: int

    def __init__(self, mask: int = 0):
        self.mask = mask
        super().__init__(
            4462,
            1, IsOnCsResponse,
            [
                Parameter("mask", "u32"),
            ])

class IsOutsideRequest(Request):
    mask: int

    def __init__(self, mask: int = 0):
        self.mask = mask
        super().__init__(
            4462,
            0, IsOutsideResponse,
            [
                Parameter("mask", "u32"),
            ])

class IsParkRequestedRequest(Request):
    def __init__(self):
        super().__init__(
            4462,
            19, IsParkRequestedResponse)

class IsReadyRequest(Request):
    def __init__(self):
        super().__init__(
            4462,
            28, IsReadyResponse)

class SetCloseToBoundaryOffsetRequest(Request):
    close_to_boundary_offset: int

    def __init__(self, close_to_boundary_offset: int = 0):
        self.close_to_boundary_offset = close_to_boundary_offset
        super().__init__(
            4462,
            7, SetCloseToBoundaryOffsetResponse,
            [
                Parameter("close_to_boundary_offset", "u16"),
            ])

class SetCloseToCsOffsetRequest(Request):
    close_to_cs_offset: int

    def __init__(self, close_to_cs_offset: int = 0):
        self.close_to_cs_offset = close_to_cs_offset
        super().__init__(
            4462,
            32, SetCloseToCsOffsetResponse,
            [
                Parameter("close_to_cs_offset", "u16"),
            ])

class SetNbrAvailableGuidesRequest(Request):
    nbr_guides: int

    def __init__(self, nbr_guides: int = 0):
        self.nbr_guides = nbr_guides
        super().__init__(
            4462,
            23, SetNbrAvailableGuidesResponse,
            [
                Parameter("nbr_guides", "u8"),
            ])

class SetPeakUpdateActiveRequest(Request):
    active: bool

    def __init__(self, active: bool = False):
        self.active = active
        super().__init__(
            4462,
            17, SetPeakUpdateActiveResponse,
            [
                Parameter("active", "bool"),
            ])

class SetPeakValueRequest(Request):
    loop: int
    value: int
    confidence: int

    def __init__(self, loop: int = 0, value: int = 0, confidence: int = 0):
        self.loop = loop
        self.value = value
        self.confidence = confidence
        super().__init__(
            4462,
            15, SetPeakValueResponse,
            [
                Parameter("loop", "u8"),
                Parameter("value", "s16"),
                Parameter("confidence", "s16"),
            ])

class SetPeriodTimeRequest(Request):
    period_time: int

    def __init__(self, period_time: int = 0):
        self.period_time = period_time
        super().__init__(
            4462,
            10, SetPeriodTimeResponse,
            [
                Parameter("period_time", "u16"),
            ])

class SetSyncSensitivityRequest(Request):
    sensitivity: int

    def __init__(self, sensitivity: int = 0):
        self.sensitivity = sensitivity
        super().__init__(
            4462,
            27, SetSyncSensitivityResponse,
            [
                Parameter("sensitivity", "u8"),
            ])

class SetTemporaryPeriodTimeRequest(Request):
    temporary_period_time: int

    def __init__(self, temporary_period_time: int = 0):
        self.temporary_period_time = temporary_period_time
        super().__init__(
            4462,
            21, SetTemporaryPeriodTimeResponse,
            [
                Parameter("temporary_period_time", "u16"),
            ])

class GetMessageRequest(Request):
    index: int

    def __init__(self, index: int = 0):
        self.index = index
        super().__init__(
            4730,
            1, GetMessageResponse,
            [
                Parameter("index", "u32"),
            ])

class GetNumberOfMessagesRequest(Request):
    def __init__(self):
        super().__init__(
            4730,
            0, GetNumberOfMessagesResponse)

class ConfirmErrorRequest(Request):
    def __init__(self):
        super().__init__(
            4586,
            9, ConfirmErrorResponse)

class GetActivityRequest(Request):
    def __init__(self):
        super().__init__(
            4586,
            3, GetActivityResponse)

class GetErrorRequest(Request):
    def __init__(self):
        super().__init__(
            4586,
            6, GetErrorResponse)

class GetForceDemoModeRequest(Request):
    def __init__(self):
        super().__init__(
            4586,
            102, GetForceDemoModeResponse)

class GetInternalStateRequest(Request):
    def __init__(self):
        super().__init__(
            4586,
            100, GetInternalStateResponse)

class GetMissionRequest(Request):
    def __init__(self):
        super().__init__(
            4586,
            13, GetMissionResponse)

class GetModeRequest(Request):
    def __init__(self):
        super().__init__(
            4586,
            1, GetModeResponse)

class GetRestrictedRequest(Request):
    def __init__(self):
        super().__init__(
            4586,
            11, GetRestrictedResponse)

class GetStateRequest(Request):
    def __init__(self):
        super().__init__(
            4586,
            2, GetStateResponse)

class IsErrorConfirmableRequest(Request):
    def __init__(self):
        super().__init__(
            4586,
            8, IsErrorConfirmableResponse)

class IsWaitingForStartTriggerRequest(Request):
    def __init__(self):
        super().__init__(
            4586,
            14, IsWaitingForStartTriggerResponse)

class PauseRequest(Request):
    def __init__(self):
        super().__init__(
            4586,
            5, PauseResponse)

class SetForceDemoModeRequest(Request):
    enable: bool

    def __init__(self, enable: bool = False):
        self.enable = enable
        super().__init__(
            4586,
            101, SetForceDemoModeResponse,
            [
                Parameter("enable", "bool"),
            ])

class SetMissionRequest(Request):
    mission_id: int

    def __init__(self, mission_id: int = 0):
        self.mission_id = mission_id
        super().__init__(
            4586,
            12, SetMissionResponse,
            [
                Parameter("mission_id", "u32"),
            ])

class SetModeRequest(Request):
    mode_of_operation: int

    def __init__(self, mode_of_operation: int = 0):
        self.mode_of_operation = mode_of_operation
        super().__init__(
            4586,
            0, SetModeResponse,
            [
                Parameter("mode_of_operation", "u8"),
            ])

class SetRestrictedRequest(Request):
    restricted: bool

    def __init__(self, restricted: bool = False):
        self.restricted = restricted
        super().__init__(
            4586,
            10, SetRestrictedResponse,
            [
                Parameter("restricted", "bool"),
            ])

class StartTriggerRequest(Request):
    def __init__(self):
        super().__init__(
            4586,
            4, StartTriggerResponse)

class SubscribeAllEventsRequest(Request):
    def __init__(self):
        super().__init__(
            4586,
            7, SubscribeAllEventsResponse)

class ClearOverrideRequest(Request):
    def __init__(self):
        super().__init__(
            4658,
            6, ClearOverrideResponse)

class GetNextStartTimeRequest(Request):
    def __init__(self):
        super().__init__(
            4658,
            1, GetNextStartTimeResponse)

class GetOverrideRequest(Request):
    def __init__(self):
        super().__init__(
            4658,
            2, GetOverrideResponse)

class GetRestrictionReasonRequest(Request):
    def __init__(self):
        super().__init__(
            4658,
            0, GetRestrictionReasonResponse)

class SetOverrideMowRequest(Request):
    duration: int

    def __init__(self, duration: int = 0):
        self.duration = duration
        super().__init__(
            4658,
            3, SetOverrideMowResponse,
            [
                Parameter("duration", "u32"),
            ])

class SetOverrideParkRequest(Request):
    duration: int

    def __init__(self, duration: int = 0):
        self.duration = duration
        super().__init__(
            4658,
            4, SetOverrideParkResponse,
            [
                Parameter("duration", "u32"),
            ])

class SetOverrideParkUntilNextStartRequest(Request):
    def __init__(self):
        super().__init__(
            4658,
            5, SetOverrideParkUntilNextStartResponse)

class AbortRequest(Request):
    def __init__(self):
        super().__init__(
            4710,
            8, AbortResponse)

class GetAllSettingsRequest(Request):
    def __init__(self):
        super().__init__(
            4710,
            5, GetAllSettingsResponse)

class GetAutoTrigCurrentRequest(Request):
    def __init__(self):
        super().__init__(
            5772,
            9, GetAutoTrigCurrentResponse)

class GetAutoTrigIntensityRequest(Request):
    def __init__(self):
        super().__init__(
            5772,
            10, GetAutoTrigIntensityResponse)

class GetAvailableRequest(Request):
    def __init__(self):
        super().__init__(
            4710,
            0, GetAvailableResponse)

class GetDetailedLogEnabledRequest(Request):
    def __init__(self):
        super().__init__(
            5772,
            1, GetDetailedLogEnabledResponse)

class GetEnabledRequest(Request):
    def __init__(self):
        super().__init__(
            4710,
            1, GetEnabledResponse)

class GetMeanCutCurrentRequest(Request):
    def __init__(self):
        super().__init__(
            5772,
            5, GetMeanCutCurrentResponse)

class GetMeanCutIntensityRequest(Request):
    def __init__(self):
        super().__init__(
            5772,
            6, GetMeanCutIntensityResponse)

class GetSensitivityRequest(Request):
    def __init__(self):
        super().__init__(
            4710,
            3, GetSensitivityResponse)

class GetStateRequest(Request):
    def __init__(self):
        super().__init__(
            5772,
            0, GetStateResponse)

class GetStatusRequest(Request):
    def __init__(self):
        super().__init__(
            4710,
            9, GetStatusResponse)

class GetUseCurrentEnabledRequest(Request):
    def __init__(self):
        super().__init__(
            5772,
            3, GetUseCurrentEnabledResponse)

class SetAvailableRequest(Request):
    available: bool

    def __init__(self, available: bool = False):
        self.available = available
        super().__init__(
            4710,
            6, SetAvailableResponse,
            [
                Parameter("available", "bool"),
            ])

class SetDetailedLogEnabledRequest(Request):
    enabled: bool

    def __init__(self, enabled: bool = False):
        self.enabled = enabled
        super().__init__(
            5772,
            2, SetDetailedLogEnabledResponse,
            [
                Parameter("enabled", "bool"),
            ])

class SetEnabledRequest(Request):
    enabled: bool

    def __init__(self, enabled: bool = False):
        self.enabled = enabled
        super().__init__(
            4710,
            2, SetEnabledResponse,
            [
                Parameter("enabled", "bool"),
            ])

class SetMeanCutCurrentRequest(Request):
    mean_cut_current_value: int
    mean_cut_current_confidence: int

    def __init__(self, mean_cut_current_value: int = 0, mean_cut_current_confidence: int = 0):
        self.mean_cut_current_value = mean_cut_current_value
        self.mean_cut_current_confidence = mean_cut_current_confidence
        super().__init__(
            5772,
            7, SetMeanCutCurrentResponse,
            [
                Parameter("mean_cut_current_value", "s32"),
                Parameter("mean_cut_current_confidence", "u8"),
            ])

class SetMeanCutIntensityRequest(Request):
    mean_cut_intensity_value: int
    mean_cut_intensity_confidence: int

    def __init__(self, mean_cut_intensity_value: int = 0, mean_cut_intensity_confidence: int = 0):
        self.mean_cut_intensity_value = mean_cut_intensity_value
        self.mean_cut_intensity_confidence = mean_cut_intensity_confidence
        super().__init__(
            5772,
            8, SetMeanCutIntensityResponse,
            [
                Parameter("mean_cut_intensity_value", "s32"),
                Parameter("mean_cut_intensity_confidence", "u8"),
            ])

class SetSensitivityRequest(Request):
    sensitivity: int

    def __init__(self, sensitivity: int = 0):
        self.sensitivity = sensitivity
        super().__init__(
            4710,
            4, SetSensitivityResponse,
            [
                Parameter("sensitivity", "u8"),
            ])

class SetUseCurrentEnabledRequest(Request):
    enabled: bool

    def __init__(self, enabled: bool = False):
        self.enabled = enabled
        super().__init__(
            5772,
            4, SetUseCurrentEnabledResponse,
            [
                Parameter("enabled", "bool"),
            ])

class StartTriggerRequest(Request):
    def __init__(self):
        super().__init__(
            4710,
            7, StartTriggerResponse)

class SubscribeAllEventsRequest(Request):
    def __init__(self):
        super().__init__(
            4710,
            10, SubscribeAllEventsResponse)

class GetAllStatisticsRequest(Request):
    def __init__(self):
        super().__init__(
            4726,
            0, GetAllStatisticsResponse)

class GetCuttingBladeUsageTimeRequest(Request):
    def __init__(self):
        super().__init__(
            4726,
            7, GetCuttingBladeUsageTimeResponse)

class GetNumberOfChargingCyclesRequest(Request):
    def __init__(self):
        super().__init__(
            4726,
            6, GetNumberOfChargingCyclesResponse)

class GetNumberOfCollisionsRequest(Request):
    def __init__(self):
        super().__init__(
            4726,
            5, GetNumberOfCollisionsResponse)

class GetTotalChargingTimeRequest(Request):
    def __init__(self):
        super().__init__(
            4726,
            3, GetTotalChargingTimeResponse)

class GetTotalCuttingTimeRequest(Request):
    def __init__(self):
        super().__init__(
            4726,
            2, GetTotalCuttingTimeResponse)

class GetTotalRunningTimeRequest(Request):
    def __init__(self):
        super().__init__(
            4726,
            1, GetTotalRunningTimeResponse)

class GetTotalSearchingTimeRequest(Request):
    def __init__(self):
        super().__init__(
            4726,
            4, GetTotalSearchingTimeResponse)

class ResetCuttingBladeUsageTimeRequest(Request):
    def __init__(self):
        super().__init__(
            4726,
            8, ResetCuttingBladeUsageTimeResponse)

class ClearStartupSequenceRequiredRequest(Request):
    def __init__(self):
        super().__init__(
            4698,
            0, ClearStartupSequenceRequiredResponse)

class GetConfigVersionStringRequest(Request):
    def __init__(self):
        super().__init__(
            4698,
            12, GetConfigVersionStringResponse)

class GetLocalHmiAvailableRequest(Request):
    def __init__(self):
        super().__init__(
            4698,
            7, GetLocalHmiAvailableResponse)

class GetModelRequest(Request):
    def __init__(self):
        super().__init__(
            4698,
            9, GetModelResponse)

class GetSerialNumberRequest(Request):
    def __init__(self):
        super().__init__(
            4698,
            10, GetSerialNumberResponse)

class GetStartupSequenceRequiredRequest(Request):
    def __init__(self):
        super().__init__(
            4698,
            2, GetStartupSequenceRequiredResponse)

class GetSwPackageVersionStringRequest(Request):
    def __init__(self):
        super().__init__(
            4698,
            22, GetSwPackageVersionStringResponse)

class GetUserMowerNameAsAsciiStringRequest(Request):
    def __init__(self):
        super().__init__(
            4698,
            5, GetUserMowerNameAsAsciiStringResponse)

class GetUserMowerNameRequest(Request):
    def __init__(self):
        super().__init__(
            4698,
            3, GetUserMowerNameResponse)

class ResetToUserDefaultRequest(Request):
    def __init__(self):
        super().__init__(
            4698,
            8, ResetToUserDefaultResponse)

class SetStartupSequenceRequiredRequest(Request):
    def __init__(self):
        super().__init__(
            4698,
            1, SetStartupSequenceRequiredResponse)

class SetUserMowerNameAsAsciiStringRequest(Request):
    name: str

    def __init__(self, name: str = ""):
        self.name = name
        super().__init__(
            4698,
            6, SetUserMowerNameAsAsciiStringResponse,
            [
                Parameter("name", "str"),
            ])

class SetUserMowerNameRequest(Request):
    name: bytes

    def __init__(self, name: bytes = bytes()):
        self.name = name
        super().__init__(
            4698,
            4, SetUserMowerNameResponse,
            [
                Parameter("name", "bytes"),
            ])

class EnableEventsRequest(Request):
    def __init__(self):
        super().__init__(
            4674,
            0, EnableEventsResponse)

class GetPowerModeRequest(Request):
    def __init__(self):
        super().__init__(
            4674,
            1, GetPowerModeResponse)

class KeepAliveRequest(Request):
    def __init__(self):
        super().__init__(
            4674,
            2, KeepAliveResponse)

class GetMaxGardenAreaRequest(Request):
    def __init__(self):
        super().__init__(
            2,
            30, GetMaxGardenAreaResponse)

class SetLoopDetectionRequest(Request):
    loop_detection: int

    def __init__(self, loop_detection: int = 0):
        self.loop_detection = loop_detection
        super().__init__(
            2,
            136, SetLoopDetectionResponse,
            [
                Parameter("loop_detection", "u8"),
            ])

class ConnectRequest(Request):
    link_id: int
    node_type: int
    name: str

    def __init__(self, link_id: int = 0, node_type: int = 0, name: str = ""):
        self.link_id = link_id
        self.node_type = node_type
        self.name = name
        super().__init__(
            20, None, ConnectResponse,
            [
                Parameter("link_id", "u32"),
                Parameter("node_type", "u32"),
                Parameter("name", "str"),
            ])

class ConnectToNodeRequest(Request):
    new_link_id: int
    node_type_filter: int
    node_name_filter: str

    def __init__(self, new_link_id: int = 0, node_type_filter: int = 0, node_name_filter: str = ""):
        self.new_link_id = new_link_id
        self.node_type_filter = node_type_filter
        self.node_name_filter = node_name_filter
        super().__init__(
            96,
            12, ConnectToNodeResponse,
            [
                Parameter("new_link_id", "u32"),
                Parameter("node_type_filter", "u32"),
                Parameter("node_name_filter", "str"),
            ])

class CreateLinkRequest(Request):
    new_link_id: int

    def __init__(self, new_link_id: int = 0):
        self.new_link_id = new_link_id
        super().__init__(
            96,
            1, CreateLinkResponse,
            [
                Parameter("new_link_id", "u32"),
            ])

class DeleteLinkRequest(Request):
    delete_link_id: int

    def __init__(self, delete_link_id: int = 0):
        self.delete_link_id = delete_link_id
        super().__init__(
            96,
            2, DeleteLinkResponse,
            [
                Parameter("delete_link_id", "u32"),
            ])

class DiscoverRequest(Request):
    traceback_id: int

    def __init__(self, traceback_id: int = 0):
        self.traceback_id = traceback_id
        super().__init__(
            18, None, DiscoverResponse,
            [
                Parameter("traceback_id", "u32"),
            ])

class GetNodeNameRequest(Request):
    def __init__(self):
        super().__init__(
            96,
            10, GetNodeNameResponse)

class GetNodeTypeRequest(Request):
    def __init__(self):
        super().__init__(
            96,
            9, GetNodeTypeResponse)

class GetVersionStringRequest(Request):
    def __init__(self):
        super().__init__(
            96,
            0, GetVersionStringResponse)

class IsPacketTypeSupportedRequest(Request):
    packet_type: int

    def __init__(self, packet_type: int = 0):
        self.packet_type = packet_type
        super().__init__(
            96,
            6, IsPacketTypeSupportedResponse,
            [
                Parameter("packet_type", "u8"),
            ])

class IsProtocolSupportedRequest(Request):
    protocol: int

    def __init__(self, protocol: int = 0):
        self.protocol = protocol
        super().__init__(
            96,
            7, IsProtocolSupportedResponse,
            [
                Parameter("protocol", "u8"),
            ])

class ListAllNodesRequest(Request):
    temp_link_id: int

    def __init__(self, temp_link_id: int = 0):
        self.temp_link_id = temp_link_id
        super().__init__(
            96,
            11, ListAllNodesResponse,
            [
                Parameter("temp_link_id", "u32"),
            ])

class RouteRawRequest(Request):
    route_port_id: int

    def __init__(self, route_port_id: int = 0):
        self.route_port_id = route_port_id
        super().__init__(
            96,
            5, RouteRawResponse,
            [
                Parameter("route_port_id", "u32"),
            ])

class RouteRequest(Request):
    route_port_id: int

    def __init__(self, route_port_id: int = 0):
        self.route_port_id = route_port_id
        super().__init__(
            96,
            3, RouteResponse,
            [
                Parameter("route_port_id", "u32"),
            ])

class SendDummyDataRequest(Request):
    length: int
    data: bytes

    def __init__(self, length: int = 0, data: bytes = bytes()):
        self.length = length
        self.data = data
        super().__init__(
            96,
            13, SendDummyDataResponse,
            [
                Parameter("length", "u16"),
                Parameter("data", "bytes"),
            ])

class SetProtocolVersionRequest(Request):
    protocol: int

    def __init__(self, protocol: int = 0):
        self.protocol = protocol
        super().__init__(
            8, None, SetProtocolVersionResponse,
            [
                Parameter("protocol", "u8"),
            ])

class UnrouteRequest(Request):
    unroute_id: int

    def __init__(self, unroute_id: int = 0):
        self.unroute_id = unroute_id
        super().__init__(
            96,
            4, UnrouteResponse,
            [
                Parameter("unroute_id", "u32"),
            ])

def get_responses():
    return [
        ChallengeResponseV2Response,
        EnterOperatorPinResponse,
        GetBlockedTimeResponse,
        GetLoginLevelResponse,
        GetRemainingLoginAttemptsResponse,
        GetSecurityCodeV2Response,
        InitiateAuthenticationV2Response,
        IsBlockedResponse,
        IsOperatorLoggedInResponse,
        IsTrustedToEnterSafetyPinResponse,
        LogoutResponse,
        SetOperatorPinResponse,
        SubscribeAllEventsResponse,
        GetAllSettingsResponse,
        GetAvailableResponse,
        GetEnabledResponse,
        GetRestrictionReasonResponse,
        GetSensitivityResponse,
        IsReadyResponse,
        SetAvailableResponse,
        SetEnabledResponse,
        SetSensitivityResponse,
        SubscribeAllEventsResponse,
        SubscribeEventChannelResponse,
        GetBatteryLevelResponse,
        GetCapacityResponse,
        GetEnergyLevelResponse,
        GetRemainingChargingTimeResponse,
        GetSimulatedEnergyLevelResponse,
        GetSimulationResponse,
        IsChargingResponse,
        SetSimulatedEnergyLevelResponse,
        SetSimulationResponse,
        DisablePairableResponse,
        ErasePairedDeviceListResponse,
        GetAdvertisingResponse,
        GetConnectedResponse,
        GetPairableResponse,
        SetAdvertisingResponse,
        SetPairableResponse,
        SubscribeAllEventsResponse,
        AddTaskResponse,
        CommitTaskTransactionResponse,
        DeleteAllTasksResponse,
        DeleteTaskResponse,
        GetNumberOfTasksResponse,
        GetTaskResponse,
        GetTimeResponse,
        SetTaskResponse,
        SetTimeResponse,
        StartTaskTransactionResponse,
        SubscribeAllEventsResponse,
        SubscribeEventChannelResponse,
        ChargingGateOffResponse,
        ChargingGateOnResponse,
        ChargingOffResponse,
        GetChargingErrorCountResponse,
        GetChargingPowerDetectedCountResponse,
        GetCurrentChargingTimeMaxResponse,
        GetCurrentChargingTimeResponse,
        GetIsBatteryChargingPreventedResponse,
        GetIsBatteryChargingResponse,
        GetIsChargingPowerDetectedResponse,
        GetIsChargingPreventedResponse,
        GetIsChargingResponse,
        GetIsInChargingStateResponse,
        GetLastChargingTimeMaxResponse,
        GetLastChargingTimeResponse,
        GetRemainingChargingTimeResponse,
        GetRemainingTotalChargingTimeResponse,
        GetSimChargingGateResponse,
        GetSimExtPowerDetectedResponse,
        GetSimIsChargingEnabledResponse,
        GetSimIsPowerConnectedResponse,
        GetSimulationResponse,
        GetStateResponse,
        GetStatusResponse,
        GetSubStateResponse,
        InjectChargingErrorResponse,
        IsChargingEnabledResponse,
        IsChargingPowerConnectedResponse,
        IsChargingPrevetnedResponse,
        IsReadyResponse,
        PreventChargingResponse,
        PreventSingleChargingResponse,
        ResetStatusResponse,
        SetSimChargingGateResponse,
        SetSimExtPowerDetectedResponse,
        SetSimIsChargingEnabledResponse,
        SetSimIsPowerConnectedResponse,
        SetSimulationResponse,
        SubscribeAllEventsResponse,
        GetAllSettingsResponse,
        GetEcoModeEnabledResponse,
        GetMowerHouseInstalledResponse,
        InitiateNewPairingResponse,
        SetEcoModeEnabledResponse,
        SetMowerHouseInstalledResponse,
        SubscribeAllEventsResponse,
        SubscribeEventChannelResponse,
        GetAllSettingsResponse,
        GetDrivePastWireResponse,
        SetDrivePastWireResponse,
        SubscribeAllEventsResponse,
        GetBoundaryCorridorResponse,
        GetCurrentDistanceResponse,
        GetNumberOfGuidesResponse,
        GetPassageCuttingEnabledResponse,
        GetStartingPointDistanceResponse,
        GetStartingPointEnabledResponse,
        GetStartingPointMaxResponse,
        GetStartingPointProportionResponse,
        GetStartingPointSettingsResponse,
        GetStartingPointWireResponse,
        GetTestErrorResponse,
        GetTestModeResponse,
        GetTestStateResponse,
        SetBoundaryCorridorResponse,
        SetPassageCuttingEnabledResponse,
        SetStartingPointDistanceResponse,
        SetStartingPointEnabledResponse,
        SetStartingPointProportionResponse,
        SetStartingPointWireResponse,
        SubscribeAllEventsResponse,
        SubscribeEventChannelResponse,
        TestAbortResponse,
        TestFollowInResponse,
        TestStartingPointResponse,
        GetAllSettingsResponse,
        GetAvailableResponse,
        GetEnabledResponse,
        GetEnabledResponseOBP,
        SetEnabledResponse,
        SetEnabledResponseOBP,
        SubscribeAllEventsResponse,
        ClearSettingsResponse,
        GetCloseToBoundaryLimitResponse,
        GetCloseToBoundaryOffsetResponse,
        GetCloseToBoundaryResponse,
        GetCloseToCsLimitResponse,
        GetCloseToCsOffsetResponse,
        GetCloseToCsResponse,
        GetInstalledLoopsResponse,
        GetLoopSideResponse,
        GetLoopSignalResponse,
        GetLoopSignalsResponse,
        GetMinMaxResponse,
        GetNbrAvailableGuidesResponse,
        GetNoLoopStatusResponse,
        GetNumSensorsResponse,
        GetOnCsStatusResponse,
        GetOutsideStatusResponse,
        GetPeakUpdateActiveResponse,
        GetPeriodTimeResponse,
        GetRawLoopSignalResponse,
        GetRawLoopSignalsResponse,
        GetSignalQualityResponse,
        GetSyncSensitivityResponse,
        GetTemporaryPeriodTimeResponse,
        IsOnCsResponse,
        IsOutsideResponse,
        IsParkRequestedResponse,
        IsReadyResponse,
        SetCloseToBoundaryOffsetResponse,
        SetCloseToCsOffsetResponse,
        SetNbrAvailableGuidesResponse,
        SetPeakUpdateActiveResponse,
        SetPeakValueResponse,
        SetPeriodTimeResponse,
        SetSyncSensitivityResponse,
        SetTemporaryPeriodTimeResponse,
        GetMessageResponse,
        GetNumberOfMessagesResponse,
        ConfirmErrorResponse,
        GetActivityResponse,
        GetErrorResponse,
        GetForceDemoModeResponse,
        GetInternalStateResponse,
        GetMissionResponse,
        GetModeResponse,
        GetRestrictedResponse,
        GetStateResponse,
        IsErrorConfirmableResponse,
        IsWaitingForStartTriggerResponse,
        PauseResponse,
        SetForceDemoModeResponse,
        SetMissionResponse,
        SetModeResponse,
        SetRestrictedResponse,
        StartTriggerResponse,
        SubscribeAllEventsResponse,
        ClearOverrideResponse,
        GetNextStartTimeResponse,
        GetOverrideResponse,
        GetRestrictionReasonResponse,
        SetOverrideMowResponse,
        SetOverrideParkResponse,
        SetOverrideParkUntilNextStartResponse,
        AbortResponse,
        GetAllSettingsResponse,
        GetAutoTrigCurrentResponse,
        GetAutoTrigIntensityResponse,
        GetAvailableResponse,
        GetDetailedLogEnabledResponse,
        GetEnabledResponse,
        GetMeanCutCurrentResponse,
        GetMeanCutIntensityResponse,
        GetSensitivityResponse,
        GetStateResponse,
        GetStatusResponse,
        GetUseCurrentEnabledResponse,
        SetAvailableResponse,
        SetDetailedLogEnabledResponse,
        SetEnabledResponse,
        SetMeanCutCurrentResponse,
        SetMeanCutIntensityResponse,
        SetSensitivityResponse,
        SetUseCurrentEnabledResponse,
        StartTriggerResponse,
        SubscribeAllEventsResponse,
        GetAllStatisticsResponse,
        GetCuttingBladeUsageTimeResponse,
        GetNumberOfChargingCyclesResponse,
        GetNumberOfCollisionsResponse,
        GetTotalChargingTimeResponse,
        GetTotalCuttingTimeResponse,
        GetTotalRunningTimeResponse,
        GetTotalSearchingTimeResponse,
        ResetCuttingBladeUsageTimeResponse,
        ClearStartupSequenceRequiredResponse,
        GetConfigVersionStringResponse,
        GetLocalHmiAvailableResponse,
        GetModelResponse,
        GetSerialNumberResponse,
        GetStartupSequenceRequiredResponse,
        GetSwPackageVersionStringResponse,
        GetUserMowerNameAsAsciiStringResponse,
        GetUserMowerNameResponse,
        ResetToUserDefaultResponse,
        SetStartupSequenceRequiredResponse,
        SetUserMowerNameAsAsciiStringResponse,
        SetUserMowerNameResponse,
        EnableEventsResponse,
        GetPowerModeResponse,
        KeepAliveResponse,
        GetMaxGardenAreaResponse,
        SetLoopDetectionResponse,
        ConnectResponse,
        ConnectToNodeResponse,
        CreateLinkResponse,
        DeleteLinkResponse,
        DiscoverResponse,
        GetNodeNameResponse,
        GetNodeTypeResponse,
        GetVersionStringResponse,
        IsPacketTypeSupportedResponse,
        IsProtocolSupportedResponse,
        ListAllNodesResponse,
        RouteRawResponse,
        RouteResponse,
        SendDummyDataResponse,
        SetProtocolVersionResponse,
        UnrouteResponse,
    ]
