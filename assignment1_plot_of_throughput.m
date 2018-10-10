%analytical curves of throughput T on transmitt probability p in a PPP wireless network, T = p(1-p)Ps(p) 
%solution for problem 5.5 in <<Stochastic Geometry for Wireless Networks by Martin Haenggi, Cambrige Press, 2013>>
d = 2;%demension
r = 1;%distance between the desired tranmitter and the receiver
lambda = 1;%insensity of the nodes
theta = 1;%SINR threshold for acceptable communication
alpha = 4;%path loss exponent
cd = pi;%pi
delta = d/alpha;%characteristic exponent
p = 0: 0.001:1;%transmitt probability
Ps = exp((-cd*lambda*p*(r^d)*(theta^delta))./(sinc(delta)));%success probability for hal-duplex PPP
Psh = exp((-cd*lambda*p.*(1-p)*(r^d)*(theta^delta))./(sinc(delta)));%success probability for full-duplex PPP
a1 = subplot(2,1,1);
T = p.*(1-p).*Ps; $throughtput in problem 5.5
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



