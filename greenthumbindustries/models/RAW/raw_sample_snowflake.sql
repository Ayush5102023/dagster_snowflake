with CTE as(
    select * from SNOWFLAKE_SAMPLE_DATA.TPCDS_SF10TCL.CUSTOMER
)

select * from CTE