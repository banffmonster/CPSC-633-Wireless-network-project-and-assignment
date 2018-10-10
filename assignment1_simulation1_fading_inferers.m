cd = pi;
I = 0;
D = 2;
r = 1;
lambda = 1;
theta = 1;
alpha = 4;
delta = D/alpha;
R = 32;
ctr =0;
pt =1;
Ps = [];
p = [];
for p = 0.05: 0.05 : 0.95
    p = p;
    ctr = 0;
    for nt = 1:1:100
        N1 = poissrnd(lambda*pi*R^2);
        UE = unifrnd(-R, R, N1, 2);
        x = UE(:,1);
        y = UE(:,2);
        d = sqrt(x.^2+y.^2);
        for nf = 1:1:10
            I = 0;
            S = 0;
            Si = 0;
            SIR = 0;
            pf = rand(1);
            if(pf > p)
                    hi = exprnd(1);
                    for n1 = 1:1:N1
                        pi = rand(1);
                        if (pi > p)
                           S = pt*exprnd(1)*((d(n1))^-alpha);
                           I = I+S;
                        end
                    end 
                    Si = pt*hi*(r^-alpha);
                    SIR = Si/I;
                    if SIR > theta
                        ctr = ctr + 1;
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

