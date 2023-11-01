"""Performance Controller Tests""" ""
import pandas as pd

from financetoolkit import Toolkit

balance_dataset = pd.read_pickle("tests/datasets/balance_dataset.pickle")
income_dataset = pd.read_pickle("tests/datasets/income_dataset.pickle")
cash_dataset = pd.read_pickle("tests/datasets/cash_dataset.pickle")
historical = pd.read_pickle("tests/datasets/historical_dataset.pickle")

toolkit = Toolkit(
    tickers=["AAPL", "MSFT"],
    historical=historical,
    balance=balance_dataset,
    income=income_dataset,
    cash=cash_dataset,
)

performance_module = toolkit.performance

# pylint: disable=missing-function-docstring


def test_get_beta(recorder):
    recorder.capture(performance_module.get_beta())
    recorder.capture(performance_module.get_beta(growth=True))
    recorder.capture(performance_module.get_beta(growth=True, lag=[1, 2, 3]))


def test_get_capital_asset_pricing_model(recorder):
    recorder.capture(performance_module.get_capital_asset_pricing_model())
    recorder.capture(performance_module.get_capital_asset_pricing_model(growth=True))
    recorder.capture(
        performance_module.get_capital_asset_pricing_model(growth=True, lag=[1, 2, 3])
    )
    recorder.capture(
        performance_module.get_capital_asset_pricing_model(show_full_results=True)
    )


def test_get_factor_asset_correlations(recorder):
    recorder.capture(performance_module.get_factor_asset_correlations())
    recorder.capture(performance_module.get_factor_asset_correlations(period="monthly"))
    recorder.capture(
        performance_module.get_factor_asset_correlations(
            factors_to_calculate=["HML", "Mkt-RF"]
        )
    )


def test_get_factor_correlations(recorder):
    recorder.capture(performance_module.get_factor_correlations())
    recorder.capture(performance_module.get_factor_correlations(period="monthly"))
    recorder.capture(
        performance_module.get_factor_correlations(
            factors_to_calculate=["HML", "Mkt-RF"]
        )
    )
    recorder.capture(
        performance_module.get_factor_correlations(exclude_risk_free=False)
    )


def test_get_fama_and_french_model(recorder):
    recorder.capture(performance_module.get_fama_and_french_model())
    recorder.capture(performance_module.get_fama_and_french_model(period="monthly"))
    recorder.capture(performance_module.get_fama_and_french_model(method="multi"))
    recorder.capture(performance_module.get_fama_and_french_model(method="simple"))

    result1, result2 = performance_module.get_fama_and_french_model(
        include_daily_residuals=True
    )
    recorder.capture(result1)
    recorder.capture(result2)

    recorder.capture(performance_module.get_fama_and_french_model(growth=True))
    recorder.capture(
        performance_module.get_fama_and_french_model(growth=True, lag=[1, 2, 3])
    )


def test_get_alpha(recorder):
    recorder.capture(performance_module.get_alpha())
    recorder.capture(performance_module.get_alpha(period="quarterly"))
    recorder.capture(performance_module.get_alpha(growth=True))
    recorder.capture(performance_module.get_alpha(growth=True, lag=[1, 2, 3]))
    recorder.capture(performance_module.get_alpha(show_full_results=True))


def test_get_jensens_alpha(recorder):
    recorder.capture(performance_module.get_jensens_alpha())
    recorder.capture(performance_module.get_jensens_alpha(period="quarterly"))
    recorder.capture(performance_module.get_jensens_alpha(growth=True))
    recorder.capture(performance_module.get_jensens_alpha(growth=True, lag=[1, 2, 3]))


def test_get_treynor_ratio(recorder):
    recorder.capture(performance_module.get_treynor_ratio())
    recorder.capture(performance_module.get_treynor_ratio(period="quarterly"))
    recorder.capture(performance_module.get_treynor_ratio(growth=True))
    recorder.capture(performance_module.get_treynor_ratio(growth=True, lag=[1, 2, 3]))


def test_get_sharpe_ratio(recorder):
    recorder.capture(performance_module.get_sharpe_ratio())
    recorder.capture(performance_module.get_sharpe_ratio(period="quarterly"))
    recorder.capture(performance_module.get_sharpe_ratio(rolling=10))
    recorder.capture(performance_module.get_sharpe_ratio(growth=True))
    recorder.capture(performance_module.get_sharpe_ratio(growth=True, lag=[1, 2, 3]))


def test_get_sortino_ratio(recorder):
    recorder.capture(performance_module.get_sortino_ratio())
    recorder.capture(performance_module.get_sortino_ratio(period="quarterly"))
    recorder.capture(performance_module.get_sortino_ratio(growth=True))
    recorder.capture(performance_module.get_sortino_ratio(growth=True, lag=[1, 2, 3]))


def test_get_ulcer_performance_index(recorder):
    recorder.capture(performance_module.get_ulcer_performance_index())
    recorder.capture(performance_module.get_ulcer_performance_index(period="quarterly"))
    recorder.capture(performance_module.get_ulcer_performance_index(growth=True))
    recorder.capture(
        performance_module.get_ulcer_performance_index(growth=True, lag=[1, 2, 3])
    )


def test_get_m2_ratio(recorder):
    recorder.capture(performance_module.get_m2_ratio())
    recorder.capture(performance_module.get_m2_ratio(period="quarterly"))
    recorder.capture(performance_module.get_m2_ratio(growth=True))
    recorder.capture(performance_module.get_m2_ratio(growth=True, lag=[1, 2, 3]))


def test_get_tracking_error(recorder):
    recorder.capture(performance_module.get_tracking_error())
    recorder.capture(performance_module.get_tracking_error(period="quarterly"))
    recorder.capture(performance_module.get_tracking_error(growth=True))
    recorder.capture(performance_module.get_tracking_error(growth=True, lag=[1, 2, 3]))


def test_get_information_ratio(recorder):
    recorder.capture(performance_module.get_information_ratio())
    recorder.capture(performance_module.get_information_ratio(period="quarterly"))
    recorder.capture(performance_module.get_information_ratio(growth=True))
    recorder.capture(
        performance_module.get_information_ratio(growth=True, lag=[1, 2, 3])
    )


def test_compount_growth_rate(recorder):
    recorder.capture(performance_module.get_compound_growth_rate())
    recorder.capture(performance_module.get_compound_growth_rate(rounding=10))
