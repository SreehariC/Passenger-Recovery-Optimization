class PNR:
    def __init__(self, pnr_number, flight_cabin, flight_number, special_requirements, is_checkin,passenger_loyalty,PAX):
        self.pnr_number = pnr_number
        self.flight_cabin  = flight_cabin
        self.flight_number = flight_number
        self.special_requirements = special_requirements.lower() == "true"
        self.is_checkin = is_checkin.lower() == "true"
        self.passenger_loyalty = passenger_loyalty
        self.PAX = int(PAX)

    def __hash__(self) -> int:
        return hash(self.pnr_number)
    
    def __repr__(self):
        return f"PNR(pnr_number='{self.pnr_number}', flight_cabin='{self.flight_cabin}', flight_number='{self.flight_number}', special_requirements='{self.special_requirements}', is_checkin={self.is_checkin}, passenger_loyalty='{self.passenger_loyalty}', PAX={self.PAX})"
    
    def get_pnr_score(self):
        return 10*self.PAX
