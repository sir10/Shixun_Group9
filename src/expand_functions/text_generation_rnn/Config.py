class Config(object):
    init_scale = 0.04
    learning_rate = 0.001
    max_grad_norm = 15
    num_layers = 3
    num_steps = 30
    hidden_size = 800 # 隐藏层size
    last_iteration = 0 # 上次训练的迭代数，从头训练写0，增量写上次的数
    iteration = 30 # 这次增加训练的迭代数
    save_freq = 1 # 每多少次自动保存
    keep_prob = 0.5
    batch_size = 128
    model_path = './Model'
    
    #parameters for generation
    save_time = 210 #从这开始是generate用的，使用第几个迭代保存的模型，必须满足上面储存的次数
    is_sample = True
    is_beams = True
    beam_size = 2
    len_of_generation = 49 # 生成的文字长度
    start_sentence = u'。\n故'# 以什么字开头