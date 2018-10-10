%simulation of success probability Ps on transmitt probability p with Rayleigh fading interferers 
cd = pi;
I = 0;
D = 2;
r = 1;
lambda = 1;
theta = 1;
alpha = 4;
delta = D/alpha;
R = 32;%radius of the PPP
ctr =0;
pt =1;
Ps = [];
p = [];
for p = 0.05: 0.05 : 0.95%increase of transmitt probability from 0.05 to 0.95
    p = p;
    ctr = 0;
    for nt = 1:1:100%iteration times
        N1 = poissrnd(lambda*pi*R^2);%generate the interferer number of PPP
        UE = unifrnd(-R, R, N1, 2);%generate the coordinates 
        x = UE(:,1);
        y = UE(:,2);
        d = sqrt(x.^2+y.^2);%distance between every undesired transmitter and the receiver
        for nf = 1:1:10%choose different senders
            I = 0;
            S = 0;%desired signal power
            Si = 0;%undesired signal power
            SIR = 0;%Signal-to-interference-ratio
            pf = rand(1);%random value of interfer node to compare with the probability p
            if(pf > p)
                    hi = exprnd(1);
                    for n1 = 1:1:N1
                        pi = rand(1);
                        if (pi > p)
                           Si = pt*exprnd(1)*((d(n1))^-alpha);%calculation of undesired signal power,exprnd(1) is the fading function
                                                                %pt is the transmit power
                           I = I+Si;
                        end
                    end 
                    S = pt*hi*(r^-alpha);%calculation of the desired signal power at the receiving node
                    SIR = S/I;
                    if SIR > theta
                        ctr = ctr + 1;%count the times that the transmitting is successful
                    end
            end
            
        end
    end
    ps = ctr/1000;
    Ps = [Ps, ps];
end
p = 0.05:0.05:0.95;
p1 = 0:0.0001:1;
figure(2)
Psa = exp((-cd*lambda*p1*(r^D)*(theta^delta))./(sinc(delta)));
plot(p1, Psa, p, Ps, '*') 
savefig('simulation1.fig')

