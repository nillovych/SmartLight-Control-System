import random
from datetime import datetime, timedelta
from listenerApp.models import LightingEvent
from django.contrib.auth.models import User

# Параметри для генерації даних
start_date = datetime(2024, 3, 27, 10, 0)
end_date = datetime(2024, 5, 27, 10, 0)
lamp_ids = ['light.virtual_light', 'light.virtual_light1']
user = User.objects.filter(username='username').first()

current_time = start_date
time_step = timedelta(minutes=10)

data = []
count = 0
previous_state = {lamp_id: False for lamp_id in lamp_ids}

while current_time < end_date:
    for lamp_id in lamp_ids:
        # Симуляція реалістичних шаблонів використання світла
        hour = current_time.hour

        if 8 <= hour < 20:
            state = random.choices([True, False], [0.8, 0.2])[0]
        else:
            state = random.choices([True, False], [0.2, 0.8])[0]

        if previous_state[lamp_id] and not state:
            if random.random() > 0.2:
                state = True
        elif not previous_state[lamp_id] and state:
            if random.random() > 0.8:
                state = False

        previous_state[lamp_id] = state

        if state:
            if 18 <= hour < 23:
                brightness = random.randint(200, 255)
            elif 6 <= hour < 8:
                brightness = random.randint(150, 200)
            else:
                brightness = random.randint(100, 200)

            color_r = random.randint(100, 255)
            color_g = random.randint(100, 255)
            color_b = random.randint(100, 255)

            event = LightingEvent(
                user=user,
                timestamp=current_time,
                lamp_id=lamp_id,
                brightness=brightness,
                color_r=color_r,
                color_g=color_g,
                color_b=color_b,
                state=state
            )
        else:
            event = LightingEvent(
                user=user,
                timestamp=current_time,
                lamp_id=lamp_id,
                state=state
            )
        data.append(event)
        count += 1
        print(f"Event #{count} created for {lamp_id}")

    current_time += time_step

print(f"Created {len(data)} lighting events.")

LightingEvent.objects.bulk_create(data)
print("Data population complete.")
