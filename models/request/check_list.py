class CheckList:
  
    def check_equal(datasets_links:list, 
                links_file:list) -> bool:
        if len(links_file) == len(datasets_links):
            return True
        return False
            
    def check_diff(datasets_links:list, 
                links_file:list) -> list:
        diff = list(set(datasets_links) - set(links_file)) + \
                        list(set(links_file) - set(datasets_links)) 
                        
        return diff