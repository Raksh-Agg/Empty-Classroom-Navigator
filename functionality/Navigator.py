def find_empty_rooms(grid_data):
    empty_rooms = {}
    for hour in range(1, 6):
        empty_rooms[hour] = []
        for row in range(5):
            for col in range(10):
                if grid_data[row][col] == 0:  # 0 indicates an empty room
                    empty_rooms[hour].append((row, col))
    return empty_rooms

def find_minimal_travel_path(roomDistances, emptyRoomsAndHours, current_room, current_hour, visited_rooms):
    if current_hour == 6:  # Base case: end of time range
        return [(current_room, current_hour)], 0

    if (current_room, current_hour) in visited_rooms:
        return None, float('inf')  # Avoid cycles in the search

    visited_rooms.add((current_room, current_hour))

    min_path, min_distance = None, float('inf')

    for next_room in emptyRoomsAndHours[current_hour]:
        if next_room != current_room:  # Avoid staying in the same room
            distance = roomDistances[current_room][next_room]
            remaining_path, remaining_distance = find_minimal_travel_path(
                roomDistances, emptyRoomsAndHours, next_room, current_hour + 1, visited_rooms.copy()
            )

            if remaining_distance + distance < min_distance:
                min_path = [(current_room, current_hour)] + remaining_path
                min_distance = remaining_distance + distance

    return min_path, min_distance

# Assume that you have already calculated roomDistances and roomOccupied based on the provided data
# And roomToAttend and hourToAttend are given as inputs (e.g., roomToAttend = 6105, hourToAttend = 2)

# Find the empty classrooms for each hour in the time range (1 to 5 except 2)
emptyRoomsAndHours = find_empty_rooms(roomOccupied)

# Find the optimal path with minimal travel distance for the student
visited_rooms = set()
optimal_path, minimal_travel_distance = find_minimal_travel_path(
    roomDistances, emptyRoomsAndHours, roomToAttend, hourToAttend, visited_rooms
)

# Print the result
print("Optimal Path:")
for room, hour in optimal_path:
    print(f"Room: {room}, Hour: {hour}")
print("Minimal Travel Distance:", minimal_travel_distance)
