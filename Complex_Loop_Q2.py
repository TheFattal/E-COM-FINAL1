def main():
    votes = []
    in_favor = 0
    against = 0
    abstentions = 0
    first_in_favor = None
    last_against = None

    subject = input("Enter the subject of the vote: ")

    print("Enter the votes from 44 countries (1 - in favor, 2 - against, 3 - abstained, 4 - veto):")

    for i in range(1, 45):  # Loop for 44 countries
        while True:
            try:
                vote = int(input(f"Country No. {i} vote: "))
                if vote not in (1, 2, 3, 4):
                    print("Invalid vote code. Please enter a number between 1 and 4.")
                    continue

                # Store the vote
                votes.append(vote)

                # Count votes
                if vote == 1:
                    in_favor += 1
                    if first_in_favor is None:
                        first_in_favor = i
                elif vote == 2:
                    against += 1
                    last_against = i
                elif vote == 3:
                    abstentions += 1
                elif vote == 4:
                    print(f"Veto vote received from Country No. {i}. Exiting...")
                    return

                break

            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    print(f"\nIn the issue of {subject}, The results are:\n")
    print(f"Number of votes in favor: {in_favor}")
    print(f"Number of votes against: {against}")
    print(f"Number of abstentions: {abstentions}")

    if first_in_favor is not None:
        print(f"First country that voted in favor: No. {first_in_favor}")
    else:
        print("No country voted in favor.")

    if last_against is not None:
        print(f"Last country that voted against: No. {last_against}")
    else:
        print("No country voted against.")


if __name__ == "__main__":
    main()
