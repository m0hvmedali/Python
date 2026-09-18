# message = input('write your command : ')
import traceback
import sys
def handle_command(self, message):
    match message:
        
        # إذا كانت الرسالة تحتوي على 3 عناصر تبدأ بـ 'BEEPER'
        case ['BEEPER', frequency, times]:
            self.beep(times, frequency)
            
        # إذا كانت الرسالة تحتوي على عنصرين تبدأ بـ 'NECK'
        case ['NECK', angle]:
            self.rotate_neck(angle)
            
        # إذا كانت الرسالة تحتوي على 3 عناصر تبدأ بـ 'LED'
        case ['LED', ident, intensity]:
            self.leds[ident].set_brightness(ident, intensity)
            
        # إذا كانت الرسالة تحتوي على 5 عناصر تبدأ بـ 'LED'
        case ['LED', ident, red, green, blue]:
            self.leds[ident].set_color(ident, red, green, blue)
            
        # الحالة الافتراضية لأي أمر آخر غير مطابق
        case _:
            print('invalid command')
# ══════════════════════════════════════════════════════════════════════════════
# NOTE: اللي فات كان المثال بتاعنا الموجود في الكتاب بس خلينا نشرح بطريقه ابسط شويه
# Topic: The main topic هو اننا عندنا بع الشروط اللي ممكن تنفذ المهمه بس بناءا على نداء منطقي اما  true او false بس هنعمل ايه لو مش عندنا نداء منطقي عندنا بداله تطبيق متشابها لو لقيت x اعمل y والا لو لقيت c اعمل e واما لو لقيت f اعمل g وهكذا 
x = int()
if x == 1:
    ...
elif x == 2:
    ...
elif x == 3:
    ...
# ---
# NOTE: ممكن نقول اننا عندنا حاجه شبهها [match : test value], [case : this value is math this pattern]
match x:
    case 1:
        ...
    case 2:
        ...
    case 3: 
        ...

# NOTE: يعنيmatch = اختبر القيمة دي \n case = هل القيمة تطابق النمط ده؟
# example <1>
command = 'write your command here:'

match command:
    case "start":
        print("starting...")
    case "stop":
        print("stoping...")
    case "pause":
        print("paused")
# ex; if command == start OUTPUT: starting
# NOTE: لحد هنا تقريبا مفيش فرق لان السؤال ممكن يترد عليه باه او لا ف برضو هنا ممكن نستخدم if condetion بس لو في حاله او نقول pattern معقد ساعتها مش هنقدر مثلا
print("="*70)
def tow_dimensional(x,y):
    match (x,y):
        case (0,0):
            print("original point")
        case (x,0):
            print("on x-axis")
        case (0, y):
            print("on y-axis")
        case (x, y):
            print("somewhere else")
    
point =tow_dimensional(0.47,0.54)
# print(point)
# ══════════════════════════════════════════════════════════════════════════════
# ╭────────────────────╮
# │ [guard with macht] │
# ╰────────────────────╯

print("="*70)

age = 10
match age:
    case age if age >=18:
        print("adult")
    case _ :
        print("minor")
# الـ pattern يطابق القيمة.
# بعدها Python تختبر الشرط:
# _ = mean anything else
# NOTE: [case _:] we can imagine this as [else:]
# ══════════════════════════════════════════════════════════════════════════════
PROMPT ="\N{cat}"

def main():
    ...
    print("type 'help' for more info")
    while True:
        try:
            match input(PROMPT):
                case 'help':
                    message = f"Python {sys.version}"
                    print(message)
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt")
        except EOFError:
            print()
            exit()
        except Exception:
            traceback.print_exc(file=sys.stdout)
if __name__ == "__main__":
    main()
