class colgee:
    resinig=0
    def __init__(self,first,last,vahed):
        self.first=first
        self.last=last
        self.vahed=vahed
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def increase_vahed(self):
        self.vahed += int(self.vahed * self.resinig)
    @classmethod
    def set_resinig_amount(cls,amount):
        cls.increase_vahed = amount
    @classmethod
    def from_str_dns(cls,dns_str):
        first,last,vahed=dns_str.split('_')
        return cls(first,last,vahed)
    @staticmethod
    def is_workday(day):
        if day.weekday==4 or day.weekday==3:
            return "today is weekday"
        else:
            return "today is workday"
dns1_str="hamid_rezai-18"
dns2_str="hamid_ghasemi-24"
new_dns1=colgee.from_str_dns(dns1_str)
new_dns2=colgee.from_str_dns(dns2-str)
print(new_dns1)
print(new_dns2)

dns1=colgee("ali","rezai",20)
dns2=colgee("reza","karohgy",20)
print(colgee.fullname(daneshjoo1))
print(colgee.fullname(daneshjoo2))

#colgee.resinig=0.2
daneshjoo2.set_resinig_amount(2)