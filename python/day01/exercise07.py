"""
    技能系统
"""

class ImpactEffect:
    """
        影响效果
    """
    def impact(self):
        pass

class DamageEffect(ImpactEffect):
    def __init__(self, value=0):
        self.value = value
    def impact(self):
        super().impact()
        print("伤害生命")

