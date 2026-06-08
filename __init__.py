# Runtime mode: keep this as paper until you have reviewed paper logs.
TRADING_MODE=paper

# Account size and risk limits for the dedicated Robinhood Agentic account.
STARTING_AGENTIC_CAPITAL=1000
MAX_DAILY_PORTFOLIO_LOSS_PCT=5
MAX_DAILY_LOSS_DOLLARS=50
MAX_POSITION_WEIGHT_PCT=20
MAX_NEW_POSITION_WEIGHT_PCT=10
MAX_DAILY_DEPLOYMENT_PCT=25
MAX_TRADES_PER_DAY=2

# Trading restrictions.
STOCKS_ONLY=true
ALLOW_OPTIONS=false
ALLOW_CRYPTO=false
ALLOW_MARGIN=false
ALLOW_SHORTS=false
DEFAULT_ORDER_TYPE=limit

# Live execution is blocked until a real approved Robinhood Agentic connector is wired in.
BROKER=paper
ROBINHOOD_MCP_URL=
ROBINHOOD_CONNECTOR_ENABLED=false

# Optional future services.
OPENAI_API_KEY=
MARKET_DATA_API_KEY=
NOTIFICATION_EMAIL=

