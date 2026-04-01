from multipledispatch import dispatch
class Opration():
    @dispatch(int,int)
    def add(self,a,b):
        print(a+b)

    @dispatch(int,int,int)
    def add(self,a,b,c):
        print(a+b+c)

op=Opration()
op.add(10,20)
op.add(10,20,30)