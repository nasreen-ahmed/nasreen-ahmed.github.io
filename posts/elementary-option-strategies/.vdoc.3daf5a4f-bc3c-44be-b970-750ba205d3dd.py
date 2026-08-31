# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
import numpy as np
import matplotlib.pyplot as plt

# Long an underlying contract at 99 
K = 99  # Original buy price
S_t = np.linspace(85,115,50)  # Current price
profit_loss_long = S_t - K

# plotting the long on underlying contract at 99 

plt.plot(S_t,profit_loss_long,label = 'Long an underlying contract at 99')

# Short an underlying contract at 99 

profit_loss_short =  K - S_t

plt.plot(S_t,profit_loss_short,label ='Short an underlying contract at 99')

plt.plot(S_t,np.linspace(0,0,50))

plt.grid()
plt.title("Expiration of Long and Short Position at 99")
plt.legend(loc="upper center")
plt.show()

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 
K = 100  # Exercise Price
S_t = np.linspace(85,110,50)  # Current price
call_option_price = 2.70

#
#for i in S_t:
#    if i < K :
#        # Here the call option will not be #exercised
#        value = - call_option_premium
#    elif i >= K:
#        # Here the call option will be #exercised 
#        value = (i - K) - #call_option_premium
#    
#    profit_loss.append(value)

profit_loss  = [np.maximum([i - K], 0) - call_option_price for i in S_t]
plt.plot(S_t,profit_loss,label = 'long a 100 call at 2.70')
plt.plot(S_t,np.linspace(0,0,50),color='green')
plt.title("Profit or Loss at expiration from the purchase of a 100 call at 2.70")
plt.legend()
plt.grid()

#
#
#
#
#
#
#
#
#
#
#


K = [95,100,105]
call_option_price = [ 5.50, 2.70,1.15]
S_t = np.linspace (85,115,50)

plt.plot(S_t, np.linspace(0, 0, 50), color='green')

for strike, premium in zip(K, call_option_price):
    profit_loss = np.maximum(S_t - strike, 0) - premium
    plt.plot(S_t, profit_loss, label=f'long a {strike} call at {premium}')

plt.title("Profit or Loss at expiration from purchasing calls at various strikes")
plt.legend()
plt.grid()
plt.show()

#
#
#
#
#
#
#
#
#
