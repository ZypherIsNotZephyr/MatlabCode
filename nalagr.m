function yy=nalagr(x,y,xx)
m=length(x);n=length(y);
if m~=n,error('����x��y�ĳ��ȱ���һ��');end
s=0;
for i = 1:n
    t=ones(1,length(xx));
    for j=[1:i-1,i+1:n]
        t=t.*(xx-x(j))/(x(i)-x(j));
    end
    s=s+t*y(i);
end
yy=s;