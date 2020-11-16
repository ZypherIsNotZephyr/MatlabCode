function x = nanewton(fname,dfname,x0,e,N)
if nargin<5,N=500;end
if nargin<4,e=1e-4;end
x =x0;x=x+2*e;k=0;
while abs(x0-x)>e&k<N,
    k = k+1;
    x0=x;x=x0-fname(x0)/dfname(x0);
    disp(x)
end
if k==N,warning('иооч');end