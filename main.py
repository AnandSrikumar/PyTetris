from src.runner import GameRunner
from memory_profiler import profile

@profile
def main():
    gr = GameRunner()
    gr.game_run()

if __name__=="__main__":
    main()