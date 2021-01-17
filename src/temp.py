import pickle as pkl

tr_d = pkl.load(open('D_total_revenue_test.pkl', 'rb'))

tr_r = pkl.load(open('R_total_revenue_test.pkl', 'rb'))

tr_f1 = [2 * (d * r)/ (d + r) for d, r in zip(tr_d, tr_r)]