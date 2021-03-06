import os

def _project_dir():
    d = os.path.dirname
    return d(d(os.path.abspath(__file__)))


def _data_dir():
    return os.path.join(_project_dir(), "data")

class Config:
    def __init__(self, config_type="mini"):
        self.opts = Options()
        self.resource = ResourceConfig()

        if config_type == "mini":
            import configs.mini as c
        elif config_type == "normal":
            import configs.normal as c
        else:
            raise RuntimeError('unknown config_type: %s' % (config_type))
        self.model = c.ModelConfig()
        self.play = c.PlayConfig()
        self.play_data = c.PlayDataConfig()
        self.trainer = c.TrainerConfig()
        self.eval = c.EvaluateConfig()

class ResourceConfig:
    def __init__(self):
        self.project_dir = os.environ.get("PROJECT_DIR", _project_dir())
        self.data_dir = os.environ.get("DATA_DIR", _data_dir())

        self.model_dir = os.environ.get("MODEL_DIR", os.path.join(self.data_dir, "model"))
        self.model_best_config_path = os.path.join(self.model_dir, "model_best_config.json")
        self.model_best_weight_path = os.path.join(self.model_dir, "model_best_weight.h5")
        self.sl_best_config_path = os.path.join(self.model_dir, "sl_best_config.json")
        self.sl_best_weight_path = os.path.join(self.model_dir, "sl_best_weight.h5")

        self.eval_model_dir = os.path.join(self.model_dir, "eval_models")
        self.eval_model1_config_path = os.path.join(self.eval_model_dir, "model1_config.json")
        self.eval_model1_weight_path = os.path.join(self.eval_model_dir, "model1_weight.h5")
        self.eval_model2_config_path = os.path.join(self.eval_model_dir, "model2_config.json")
        self.eval_model2_weight_path = os.path.join(self.eval_model_dir, "model2_weight.h5")
        self.model1_name = "model1"
        self.model2_name = "model2"
        self.rival_model_config_path = os.path.join(self.model_dir, "rival_config.json")
        self.rival_model_weight_path = os.path.join(self.model_dir, "rival_weight.h5")

        self.play_data_dir = os.path.join(self.data_dir, "play_data")
        self.play_data_filename_tmpl = "play_%s.json"
        self.self_play_game_idx_file = os.path.join(self.data_dir, "play_data_idx")
        self.play_record_filename_tmpl = "record_%s.qp"
        self.play_record_dir = os.path.join(self.data_dir, "play_record")

        self.log_dir = os.path.join(self.project_dir, "logs")
        self.main_log_path = os.path.join(self.log_dir, "main.log")
        self.opt_log_path = os.path.join(self.log_dir, "opt.log")
        self.play_log_path = os.path.join(self.log_dir, "play.log")
        self.sl_log_path = os.path.join(self.log_dir, "sl.log")

        self.sl_data_dir = os.path.join(self.data_dir, "sl_data")
        self.sl_data_gameinfo = os.path.join(self.sl_data_dir, "gameinfo.csv")
        self.sl_data_move = os.path.join(self.sl_data_dir, "moves.csv")

    def create_directories(self):
        dirs = [self.project_dir, self.data_dir, self.model_dir, self.play_data_dir, self.log_dir,
                self.play_record_dir, self.eval_model_dir]
        for d in dirs:
            if not os.path.exists(d):
                os.makedirs(d)

class Options:
    new = False
    light = True
    evaluate = False

class PlayWithHumanConfig:
    def __init__(self):
        self.simulation_num_per_move = 100
        self.thinking_loop = 1
        self.c_puct = 1
        self.search_threads = 2
        self.noise_eps = 0
        self.tau_decay_rate = 0

    def update_play_config(self, pc):
        pc.simulation_num_per_move = self.simulation_num_per_move
        pc.thinking_loop = self.thinking_loop
        pc.c_puct = self.c_puct
        pc.noise_eps = self.noise_eps
        pc.tau_decay_rate = self.tau_decay_rate
        pc.search_threads = self.search_threads


