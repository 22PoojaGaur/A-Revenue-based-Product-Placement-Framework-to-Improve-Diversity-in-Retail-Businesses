



beta = 0.3
import pickle as pkl 
[tr_r + beta * tr_dr for (tr_r, tr_dr) in zip(pkl.load(open('R_total_revenue_test.pkl', 'rb')), pkl.load(open('DR_total_revenue_test.pkl', 'rb')))]