# kindle book metadata + review cleaning
This repo steps to clean kindle book metadata and review.\
### Datasets:
* Amazon Kindle’s reviews, available from [Kaggle website](https://www.kaggle.com/bharadwaj6/kindle-reviews).
* Amazon Kindle metadata, available from [UCSD website](http://jmcauley.ucsd.edu/data/amazon/) (original dataset).
* Amazon Kindle metadata, cleaned by prof Anh. (prof dataset)


## Clean original, prof datasets
### Steps:
1. Clean original dataset, prof datasets seperately using
    * `./data_cleaning/clean_original_metadata.ipynb` : clean original dataset
    * `./data_cleaning/clean_prod_data.ipynb`: clean prof dataset
2. Combine cleaned original and prof dataset using `./data_cleaning/combined.ipynb`

## Aggregate review information to `book_review_stats.csv`
```
"ASIN";"review number";"average rating";"total rating"
"B000JMKX4W";"11";"3.5455";"39"
```

## Post processing + combine review info and book metadata
### Post processing agenda
* Eliminate recommended ASIN that does not exists
* Incorparate review information to book metadata
* Clean illegal strings and characters
* Get all categories and its count

### Data
* Input: `./post-processing-metadata/original_data/`, combined output from last step
* Output: `./post-processing-metadata/numerical_output/`
* Intermidiate: make sure to create these folders before run the following steps
    * `./post-processing-metadata/output/`
    * `./post-processing-metadata/combined_output/`

### Steps:
1. Run `./post-processing-metadata/find_categories.py` to get all category and counts. Results stored in `./post-processing-metadata/catogory_count`

    ```
    {"category": "Self-Help", "book_count": 2630}
    ```
2. Run `./post-processing-metadata/get_all_asin.py` to get all existing book asins. Results stored in `./post-processing-metadata/all_books`
    ```
    B000PSJ8PK
    B000QCQ9GG
    B000UZJQ9G
    ...
    ```
3. Run `./post-processing-metadata/clean_book_metadata.py` to clean book metadata: eliminate non-exist asin in recommendation fields, eliminate illegal strings etc.
    * Input: `./post-processing-metadata/original_data/`
    * Output: `./post-processing-metadata/output/`

4. Run `./post-processing-metadata/combine.py` to incorperate review info in book metadata
    * Input: `./post-processing-metadata/output/`
    * Output: `./post-processing-metadata/combined_output/`

5. Run `./post-processing-metadata/clean_review.py` to convert review strings to numbers
    * Input: `./post-processing-metadata/combined_output/`
    * Output: `./post-processing-metadata/numerical_output/`
### Final output:
```
{
    "asin": "B0015YEQ6O", 
    "price": 3.99, 
    "imUrl": "http://ecx.images-amazon.com/images/I/41FF%2Bi1%2BI9L._BO2,204,203,200_PIsitb-sticker-v3-big,TopRight,0,-55_SX278_SY278_PIkin4,BottomRight,1,22_AA300_SH20_OU01_.jpg", 
    "description": "", 
    "related": ["B00K9NWRHW"], 
    "rank": 616872, 
    "title": "Enjoying the Show (Wicked Warrens Book 1)", 
    "author": "Marie Harte", 
    "category": "Romance", 
    "review_number": 32, 
    "rating_average": 4.4688, 
    "rating_total": 143.0
}
```