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



profit_loss_95 = [np.maximum(i-K1) - call_option_price_95 for i in S_t]
profit_loss_100 = [np.maximum(i-K2) - call_option_price_100 for i in S_t]
profit_loss_105 = [np.maximum(i-K3) - call_option_price_105 for i in S_t]

plt.plot(S_t,profit_loss_95,label = 'long a 95 call at 5.50')
plt.plot(S_t,profit_loss_100,label = 'long a 95 call at 5.50')
plt.plot(S_t,profit_loss_105,label = 'long a 95 call at 5.50')
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
