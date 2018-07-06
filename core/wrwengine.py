import time
import asyncio

class WrwGameEngine(object):
    def __init__(self):
        self.players = WrwPlayersManagement()
        self.stateEng = WrwStateEngine()
        self.mainloop = asyncio.get_event_loop()
        self.game_end_sign = asyncio.Future()
    def start_game(self):
        self.stateEng.day_night_shift(self.game_end_sign)
        self.mainloop.run_until_complete(self.game_end_sign)
        print(self.game_end_sign.result())
        self.mainloop.close()

class WrwStateEngine(object):
    """
    Control and store all the states and changes of the wrw game.
    """
    def __init__(self, **kwargs):
        self._round = 0
        self._game_rules = [] # Define the game rules

    def day_night_shift(self, future):
        self._round +=1
        asyncio.ensure_future(self.roundresult(future))        

    async def roundresult(self, future):
        if self._round %10 == 0:
            print(self._round)
            await asyncio.sleep(1)
        if self._round > 50:
            future.set_result("Future is done!")
            self.gameend()
        else:
            self.day_night_shift(future)

    def gameend(self):
        print("Game over!")

class WrwGameRules(object):
    def __init__(self):
        pass


class WrwPlayersManagement(object):
    def __init__(self):
        self.all_players = set()
    def init_player(self):
        pass

class WrwBasicEventLoop(object):
    def __init__(self):
        self.be_loop = asyncio.get_event_loop()
        self.be_loop_completion = asyncio.Future()
    def start_loop(self):
        pass


class WrwNightLoop(WrwBasicEventLoop):
    def __init__(self):
        pass
    def start_loop(self):
        self.be_loop.run_until_complete(self.be_loop_completion)
        
class WrwDaytimeLoop(WrwBasicEventLoop):
    def __init__(self):
        pass
    def start_loop(self):
        pass
