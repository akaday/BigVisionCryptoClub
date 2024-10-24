from resto_app.payments.crypto_payments import process_payment
from resto_app.reservations.booking import reserve_table

def main():
    # Example Usage
    process_payment("BTC", 0.01)
    reserve_table("John Doe", "2024-10-30", 2)

if __name__ == "__main__":
    main()
