function[x,y]=func10b(dyfun,xspan,y0,h)
x=xspan(1):h:xspan(2);y(1)=y0;
for n=1:length(x)-1
    k1=dyfun(x(n),y(n));
    y(n+1)=y(n)+h*k1;
k2=dyfun(x(n+1),y(n+1));
y(n+1)=y(n)+h*(k1+k2)/2;
end
x=x';
y=y';
