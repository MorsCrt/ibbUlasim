from msilib import datasizemask
import file_paths

class CheckList:
    def check_empty():
        import scraper
        if len(file_paths.links_file)==0:
            with open(file_paths.links_file_path,"w") as w:
                for x in scraper.datasets_links:
                    w.write(x+"\n")
                w.close()
        
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