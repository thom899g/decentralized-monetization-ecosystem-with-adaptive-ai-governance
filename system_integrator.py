import logging
from typing import Dict, Any
from strategy_generator import StrategyGenerator
from testing_module import TestingModule
from optimization_engine import OptimizationEngine
from governance_layer import GovernanceLayer

class SystemIntegrator:
    def __init__(self):
        self.logger = logging.getLogger("SystemIntegrator")
        self.strategy_generator = StrategyGenerator()
        self.testing_module = TestingModule()
        self.optimization_engine = OptimizationEngine()
        self.governance_layer = GovernanceLayer()
    
    def execute_pipeline(self, data: Dict) -> Dict:
        """Executes the entire pipeline from strategy generation to governance."""
        try:
            # Generate strategies
            self.strategy_generator.generate_strategies(data)
            
            # Test each strategy
            test_results = {}
            for strategy in self.strategy_generator.strategies:
                results = self.testing_module.test_strategy(strategy)
                test_results[strategy.id] = results
            
            # Optimize strategies based on testing
            optimized_strategies = []
            for strategy in self.strategy_generator.strategies:
                optimized = self.optimization_engine.optimize(strategy, test_results[strategy.id])
                optimized_strategies.append(optimized)
            
            # Enforce governance
            compliant_strategies = []
            for strategy in optimized_strategies:
                if self.governance_layer.enforce_compliance(strategy):
                    compliant_strategies.append(strategy)
            
            return {"compliant_strategies": compliant_strategies}
        except Exception as e:
            self.logger.error(f"Pipeline execution failed: {str(e)}")
            raise