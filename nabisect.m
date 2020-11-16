function x =nabisect(fname,a,b,e)
if nargin<4,e=1e-4;end;
fa=fname(a);fb=fname(b);
if fa*fb>0,error('Á½µãÒìºÅ');end
x=(a+b)/2
while(b-a)>(2*e)
    fx = fname(x)
    if fa*fx<0,b=x;fb=fx;else a=x;fa=fx;end
    x=(a+b)/2
end