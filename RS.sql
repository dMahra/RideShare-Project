CREATE TABLE "Booking" (
	"Book_id"	INTEGER NOT NULL,
	"Amount"	INTEGER NOT NULL,
	"Pay_type"	TEXT NOT NULL,
	"Booking_date"	TEXT NOT NULL,
	"Drive_id"	INTEGER NOT NULL,
	PRIMARY KEY("Book_id")
);
CREATE TABLE "Customer" (
	"Customer_id"	INTEGER NOT NULL,
	"Cur_address"	TEXT NOT NULL,
	"Name"	TEXT NOT NULL,
	"Phone_number"	INTEGER NOT NULL,
	"Password"	TEXT NOT NULL,
	PRIMARY KEY("Customer_id")
);
CREATE TABLE "Driver" (
	"Drive_id"	INTEGER NOT NULL,
	"Name"	TEXT NOT NULL,
	"Birthday" TEXT,
	"Phone_number"	INTEGER NOT NULL,
	"Password"	TEXT NOT NULL,
	"Car_id"	INTEGER NOT NULL,
	PRIMARY KEY("Drive_id")
);
CREATE TABLE "Trip" (
	"Trip_id"	INTEGER NOT NULL,
	"Destination"	TEXT NOT NULL,
	"Duration"	INTEGER NOT NULL,
	"Arrival_time"	TEXT NOT NULL,
	"Booking_id"	INTEGER NOT NULL,
	PRIMARY KEY("Trip_id")
);
CREATE TABLE "Vehicle" (
	"Car_id"	INTEGER NOT NULL,
	"registration_#"	INTEGER NOT NULL,
	"type"	TEXT NOT NULL,
	PRIMARY KEY("Car_id")
);

