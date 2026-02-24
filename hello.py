from abc import ABC, abstractmethod
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# 1. الكلاس المجرد (الواجهة/Interface) - يفرض شروطاً
class ISmartFeatures(ABC):
    @abstractmethod
    def connect_to_wifi(self):
        """يجب على كل قطعة ذكية الاتصال بالواي فاي"""
        pass

# 2. الكلاس العادي (الأب) - يعطي صفات جاهزة
class Sofa:
    def __init__(self, model, color):
        self.model = model
        self.color = color
    
    def display_info(self):
        print(f"Sofa Model: {self.model}, Color: {self.color}")

# 3. الكلاس الابن - يورث من الاثنين معاً (Multiple Inheritance)
class SmartAnshasiSofa(Sofa, ISmartFeatures):
    def __init__(self, model, color, battery_level):
        # استدعاء كونسركتور الكلاس العادي
        super().__init__(model, color)
        self.battery = battery_level

    # تنفيذ الدالة المجردة (إجباري)
    def connect_to_wifi(self):
        print(f"Connecting {self.model} to Anshasi Smart Home Hub...")

    def show_battery(self):
        print(f"Battery level: {self.battery}%")

# --- التجربة ---
my_smart_sofa = SmartAnshasiSofa("Anshasi-V1", "Midnight Blue", 85)

my_smart_sofa.display_info()     # جاءت من Sofa (العادي)
my_smart_sofa.connect_to_wifi() # تم تنفيذها التزاماً بـ ISmartFeatures (المجرد)
my_smart_sofa.show_battery()    # خاصة بالابن نفسه