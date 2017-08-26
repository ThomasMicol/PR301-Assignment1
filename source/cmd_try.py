from cmd import Cmd

class Quitter(Cmd):

    def do_add(self,s):
        l = s.split()
        if len(l)!=2:
           print ("*** invalid number of arguments")
           return
        try:
           l = [int(i) for i in l]
        except ValueError:
           print ("*** arguments should be numbers")
           return
        print (l[0]+l[1])

 #   do_q = do_quit

    def help_add(self):
        print ('add two integral numbers')


if __name__ == "__main__":
    quitter = Quitter()
    quitter.cmdloop()
