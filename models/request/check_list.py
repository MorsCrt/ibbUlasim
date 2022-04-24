import file_paths

def check_diff():
    diff = list(set(file_paths.ibb_csv_links) - set(file_paths.link_formatted)) + \
                    list(set(file_paths.link_formatted) - set(file_paths.ibb_csv_links)) 
    return diff

def check_empty():
    if len(file_paths.links_file)==0:
        with open(file_paths.links_file_path,"w") as w:
            for x in file_paths.ibb_csv_links:
                w.write(x+"\n")
            w.close()
        return True
