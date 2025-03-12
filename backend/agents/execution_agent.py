from . import BaseAgent, datetime


class ExecutionAgent(BaseAgent):
  def __init__(self, name, broker_api_key=None, paper_trading=True):
    super().__init__(name)
    self.broker_api_key = broker_api_key
    self.paper_trading = paper_trading
    self.orders = []
    self.portfolio = {}
    self.cash = 10000.0  # 初始资金（模拟）

  def run(self):
    # 主要是响应订单请求
    pass

  def receive_message(self, message):
    if message['type'] == 'trade_order':
      symbol = message['payload'].get('symbol')
      action = message['payload'].get('action')
      quantity = message['payload'].get('quantity')

      if self.paper_trading:
        # 模拟交易执行
        self._execute_paper_trade(symbol, action, quantity)
      else:
        # 实际交易
        self._execute_real_trade(symbol, action, quantity)

  def _execute_paper_trade(self, symbol, action, quantity):
    # 获取当前价格
    self.send_message('data_agent', 'get_data', {'symbol': symbol})
    # 这里简化了，实际上应该等待数据响应后再执行
    # 假设价格为100
    price = 100

    if action == 'buy':
      cost = price * quantity
      if cost <= self.cash:
        self.cash -= cost
        self.portfolio[symbol] = self.portfolio.get(symbol, 0) + quantity
        self.orders.append({
            'symbol': symbol,
            'action': 'buy',
            'quantity': quantity,
            'price': price,
            'timestamp': datetime.now()
        })
        # 通知其他代理
        self.send_message('all', 'trade_executed', {
            'symbol': symbol,
            'action': 'buy',
            'quantity': quantity,
            'price': price
        })
    elif action == 'sell':
      if symbol in self.portfolio and self.portfolio[symbol] >= quantity:
        self.cash += price * quantity
        self.portfolio[symbol] -= quantity
        self.orders.append({
            'symbol': symbol,
            'action': 'sell',
            'quantity': quantity,
            'price': price,
            'timestamp': datetime.now()
        })
        # 通知其他代理
        self.send_message('all', 'trade_executed', {
            'symbol': symbol,
            'action': 'sell',
            'quantity': quantity,
            'price': price
        })

  def _execute_real_trade(self, symbol, action, quantity):
    # 实现与实际经纪商API的集成
    pass
