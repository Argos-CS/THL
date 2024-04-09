import pandas as pd
import yfinance as yf

def get_option_chain(ticker):
    """
    Função para obter a cadeia de opções de um ticker específico.
    """
    ticker = yf.Ticker(ticker)
    opt = ticker.option_chain()
    return opt.puts

def find_calendar_spreads(puts):
    """
    Função para encontrar spreads de calendário em uma lista de opções de venda.
    """
    spreads = []
    for i in range(len(puts) - 1):
        for j in range(i + 1, len(puts)):
            if puts.iloc[i].strike == puts.iloc[j].strike:
                spread = {
                    'strike': puts.iloc[i].strike,
                    'short_term_expiry': puts.iloc[i].expiry,
                    'long_term_expiry': puts.iloc[j].expiry,
                    'entry_cost': puts.iloc[j].lastPrice - puts.iloc[i].lastPrice
                }
                spreads.append(spread)
    return spreads

def main():
    """
    Função principal para executar o script.
    """
    ticker = 'AAPL'  # Substitua por qualquer ticker de sua escolha.
    puts = get_option_chain(ticker)
    spreads = find_calendar_spreads(puts)
    spreads = sorted(spreads, key=lambda x: x['entry_cost'])
    df = pd.DataFrame(spreads)
    print(df)

if __name__ == "__main__":
    main()
