-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/l9T8dw
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

CREATE TABLE "deals" (
    "Deal_Table_Record_ID" int   NOT NULL,
    "Deal_Created_at" timestamp   NOT NULL,
    "Deal_Updated_at" timestamp   NOT NULL,
    "Deal_Original_Due_at" timestamp   NOT NULL,
    "Deal_Due_at" timestamp   NOT NULL,
    "Deal_assigned_at" timestamp   NOT NULL,
    "Mockups_ready_at" timestamp   NOT NULL,
    "Mockup_due_date" timestamp   NOT NULL,
    "Hs_quantity" int   NOT NULL,
    "Hs_client_type" varchar(255)   NOT NULL,
    "Po_number" int   NOT NULL,
    "Portal_created" timestamp   NOT NULL,
    "Hs_design_difficulty" varchar(255)   NOT NULL,
    "Automation_tool" int   NOT NULL,
    "Hs_dealtype" varchar(255)   NOT NULL,
    "Deal_Created_on" timestamp   NOT NULL,
    CONSTRAINT "pk_deals" PRIMARY KEY (
        "Deal_Table_Record_ID"
     )
);

CREATE TABLE "deals_mockups" (
    "Deals_mockups_ID" int   NOT NULL,
    "Deal_ID" int   NOT NULL,
    "Mockup_ID" int   NOT NULL,
    "Deals_Mockups_created_at" timestamp   NOT NULL,
    "Deals_Mockups_updated_at" timestamp   NOT NULL,
    CONSTRAINT "pk_deals_mockups" PRIMARY KEY (
        "Deals_mockups_ID"
     )
);

CREATE TABLE "mockups" (
    "Mockup_ID" int   NOT NULL,
    "mockup_created_at" timestamp   NOT NULL,
    "Mockup_updated_at" timestamp   NOT NULL,
    "Version_number" int   NOT NULL,
    "Design_number" int   NOT NULL,
    "Chassis" int   NOT NULL,
    "Previously_ordered" timestamp   NOT NULL,
    "Design_source" varchar(255)   NOT NULL,
    "Designer_ID" int   NOT NULL,
    "Parent_mockup_ID" int   NOT NULL,
    CONSTRAINT "pk_mockups" PRIMARY KEY (
        "Mockup_ID"
     )
);

CREATE TABLE "cart_items" (
    "cart_items_id" int   NOT NULL,
    "Created_at" timestamp   NOT NULL,
    "Quantity" int   NOT NULL,
    "Mockup_ID" int   NOT NULL,
    "Mockup_version" int   NOT NULL,
    "Sock_unit_price" float   NOT NULL,
    "Pkg_unit_price" float   NOT NULL,
    "Product_ID" int   NOT NULL,
    "Unit_price" float   NOT NULL,
    "Cart_total" int   NOT NULL,
    "Created_on" timestamp   NOT NULL,
    CONSTRAINT "pk_cart_items" PRIMARY KEY (
        "cart_items_id"
     )
);

CREATE TABLE "revisions" (
    "revisions_ID" int   NOT NULL,
    "Mockup_ID" int   NOT NULL,
    "Version_number" int   NOT NULL,
    "Completed_at" timestamp   NOT NULL,
    "Created_at" timestamp   NOT NULL,
    "Updated_at" timestamp   NOT NULL,
    "Packaging_ID" int   NOT NULL,
    "Product_ID" int   NOT NULL,
    "Sock_pair_ID" int   NOT NULL,
    "Base_version" int   NOT NULL,
    "Read_at" timestamp   NOT NULL,
    CONSTRAINT "pk_revisions" PRIMARY KEY (
        "revisions_ID"
     )
);

CREATE TABLE "mfg_products" (
    "mfg_products_ID" int   NOT NULL,
    "Mockup_ID" int   NOT NULL,
    "Created_at" timestamp   NOT NULL,
    "Updated_at" timestamp   NOT NULL,
    "Packaging_ID" int   NOT NULL,
    "Product_ID" int   NOT NULL,
    "Sock_pair_ID" int   NOT NULL,
    "Created_on" timestamp   NOT NULL,
    "Mockup_version" int   NOT NULL,
    "Quantity" int   NOT NULL,
    "Product_info_ID" int   NOT NULL,
    CONSTRAINT "pk_mfg_products" PRIMARY KEY (
        "mfg_products_ID"
     )
);

ALTER TABLE "deals_mockups" ADD CONSTRAINT "fk_deals_mockups_Deal_ID" FOREIGN KEY("Deal_ID")
REFERENCES "deals" ("Deal_Table_Record_ID");

ALTER TABLE "deals_mockups" ADD CONSTRAINT "fk_deals_mockups_Mockup_ID" FOREIGN KEY("Mockup_ID")
REFERENCES "cart_items" ("Mockup_ID");

ALTER TABLE "mockups" ADD CONSTRAINT "fk_mockups_Mockup_ID" FOREIGN KEY("Mockup_ID")
REFERENCES "deals_mockups" ("Mockup_ID");

ALTER TABLE "cart_items" ADD CONSTRAINT "fk_cart_items_Mockup_ID" FOREIGN KEY("Mockup_ID")
REFERENCES "mockups" ("Mockup_ID");

ALTER TABLE "revisions" ADD CONSTRAINT "fk_revisions_Mockup_ID" FOREIGN KEY("Mockup_ID")
REFERENCES "mockups" ("Mockup_ID");

