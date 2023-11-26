def activity_selection(activities):
    activities.sort(key=lambda x: x[0])
    
    selected_activities = []
    selected_activity = activities[0]
    
    for activity in activities[1:]:
        if activity[0] >= selected_activity[1]:
            selected_activities.append(selected_activity)
            selected_activity = activity
    
    selected_activities.append(selected_activity)
    
    return selected_activities

activities = [(1, 3), (2, 5),(1, 6), (3, 6), (5, 8), (7, 10)]
selected = activity_selection(activities)
print("Selected Activities :", selected)

