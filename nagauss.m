function x = nagauss1(a,b,flag)
%��; ˳���˹��ȥ�������Է���ax=b
%a ϵ������ b �Ҷ�������
%flag ��Ϊ0������ʾ�м���� ������ʾĬ��ֵΪ0
%x��������
if nargin<3,flag=0;end
n=length(b);a=[a,b];
%��Ԫ
for k=1:(n-1)
    a((k+1):n,(k+1):(n+1)) = a((k+1):n,(k+1):(n+1))...
        -a((k+1):n,k)/a(k,k)*a(k,(k+1):(n+1));
    a((k+1):n,k) = zeros(n-k,1);
    if flag==0,a,end
end
%�ش�
x=zeros(n,1);
x(n)=a(n,n+1)/a(n,n);
for k=n-1:-1:1
    x(k) = (a(k,n+1)-a(k,(k+1):n)*x((k+1):n))/a(k,k);
end