
# If needed import constants.py

class PNR:
    def __init__(self, pnr_number,inv_list, sub_class_list, special_requirements,PAX, passenger_loyalty):

        # inv_list -> list of inventory ids for this pnr (all the connecting flights)
        # sub_class_list -> list of all the subclasses this PNR is travelling in for each leg of journey
        self.pnr_number = pnr_number
        self.inv_list = inv_list
        self.sub_class_list  = sub_class_list
        self.special_requirements = special_requirements 
        self.PAX = int(PAX)
        self.passenger_loyalty = passenger_loyalty
        

    def __hash__(self) -> int:
        return hash(self.pnr_number)
    
    def __eq__(self, other):
        return isinstance(other, PNR) and self.pnr_number == other.pnr_number
    
    def __repr__(self):
        return f"PNR('{self.pnr_number}', {self.inv_list}, {self.cabin_list}, {self.PAX})"
    
    def get_loyalty_score(self):
        """
            Returns the score associated with the loyalty string (ex. Gold Silver Platinum)
        """
        # Assuming that constants.py has a dictionary where key is string(loyalty_class) and value is score for that loyalty
        return loyalty_dict[self.loyalty]

    def get_ssr_score(self):
        """
            Returns the score associated with this SSR string (ex. WCHR , DEAF )
            
        """
        if(self.special_requirements == "Grade1"):
            return PNR_SSR
        elif (self.special_requirements=="Grade2"):
            return PNR_SSR/2
        pass
    
    def get_pnr_score(self):
        """
        Calculates the PNR score for each PNR.
        Calculation done as follows: score = a*s1 + b*s2 + c*s3
        where,  s1 = PNR_SSR
                s2 = PNR_loyalty
                s3 = PNR_pax
        """
        #TODO normalize s1 , s2 ,s3 if required 
        s1 = self.get_ssr_score()
        s2 = self.get_loyalty_score()
        s3 = self.PAX * PNR_pax
        return s1 + s2 + s3

        pass