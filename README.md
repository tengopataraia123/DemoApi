# Unilab Demo API
რეპოზიტორია წარმოადგენს NLTK ბიბლიოთეკის გარშემო აწყობილ საცდელ API-ს


## Documentation

ვებ სერვისის გამოყენება შეგიძლიათ შესაბამის მისამართზე მოთხოვნის გასაგზავნად.

მოთხოვნის მისამართი და მოთხოვნის body შეგიძლიათ ნახოთ მეთოდების ჩამონათვალში

##Methods:

**TemSentenceTokenizer**
>
> სერვისი მოთხოვნილ წინადადებას უკეთებს ტოკენიზაციას და აბრუნებს ტოკენიზებულ სიას
> ``` 
> endpoint: _/TemSenTok_
> type: GET 
> body: {
> "sentence" : "This is my demo sentence"
> } 
> ```
> 
**FrequencyDistribution**
>
> სერვისი მოთხოვნილ ტექსტს უკეთებს ტოკენიზაციას და აბრუნებს სიტყვების სიხშირის განაწილების სიას
> ``` 
> endpoint: _/FreqDist_
> type: GET 
> body: {
> "text" : "This is my demo text"
> } 
> ```

**GroupingMultiplePatters**
>
> სერვისი მოთხოვნილ ტექსტს უკეთებს ტოკენიზაციას და აბრუნებს სიმბოლოებისგან გაწმენდილ ტექსტს
> ``` 
> endpoint: _/GMultiplePatterns_
> type: GET 
> body: {
> "text" : "This is my demo sentence"
> } 
> ```

**Chunk_CleanSentences**
>
> Devides and clears the sentence of punctuation marks and builds a dependency tree on each sentence. Allocates its own names and verbs.
> ``` 
> endpoint: _/Chunk
> type: GET 
> body: {
> "text" : "Any Text"