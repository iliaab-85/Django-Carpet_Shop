
class UserAuth():
    def __init__(self):
        self.State = False
        self.User = None
    def StateLogin(self,request):
        if request.user.is_authenticated:
            self.User = request.user
            self.State = True
            self.id = request.user
            dic = {"State":self.State,"User":self.User,"id":self.id}
            return dic
        else:
            self.User = None
            self.State = False
            self.id = 0
            dic = {"State":self.State,"User":self.User,"id":self.id}
            return dic