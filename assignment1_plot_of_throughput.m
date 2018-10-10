d = 2;
r = 1;
lambda = 1;
theta = 1;
alpha = 4;
cd = pi;
delta = d/alpha;
p = 0: 0.001:1;
Ps = exp((-cd*lambda*p*(r^d)*(theta^delta))./(sinc(delta)));
Psh = exp((-cd*lambda*p.*(1-p)*(r^d)*(theta^delta))./(sinc(delta)));
a1 = subplot(2,1,1);
T = p.*(1-p).*Ps; 
figure(1)
plot(p, T)
title('half-duplex')
xlabel('p')
ylabel('T')
Th = p.*(1-p).*Psh; 
a2 = subplot(2,1,2);
plot(a2, p, Th)
title('full-duplex')
xlabel('p')
ylabel('T')
savefig('5_5.fig')



