from itertools import islice

if __name__ == "view":
    
    def views(top_results):
        by_view =[]
        sorted_views = list(islice(sorted(list(top_results.values()), reverse=True), 3))   
        for key, value in top_results.items():
            if value in sorted_views:
                by_view.append(key)
                
        return by_view