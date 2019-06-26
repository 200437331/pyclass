def howmanybirds(bird_name, bird_weight, fruit_name, fruit_weight, bodyweight_percentage):
    carry = (bird_weight * bodyweight_percentage)
    birds = (fruit_weight / carry)
    print("It would take " + str(birds) + " " + bird_name + "s to carry one " + fruit_name)
    return (fruit_weight / carry)

print(howmanybirds("Swallow", 60, "coconut", 1450, (1 / 3)))
