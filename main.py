import argparse
import save_data_to_csv as save
# import tech_ind_model as train
# import trading_algo as algo


x = -1
while x != 0:
    print('----------Choose an action\n----------')
    print('1: Get and save data\n2: Training\n3: make prediction' )
    print('q to exit')
    x = input('Action: ')
    if x == '1':
        index = input('index: ')
        time_w = input('choose time window: intraday, daily, daily_adj: ')
        save.save_dataset(symbol=index, time_window=time_w)
    elif x == '2':
        import tech_ind_model
    elif x == '3':
        import trading_algo
        #algo.run()
        exit()
    elif x == 'q':
        exit()
    else:
        print('not valid')
