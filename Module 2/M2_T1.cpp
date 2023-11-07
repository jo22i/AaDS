#include <iostream>
#include <string>

class SplayTree
{
    uint64_t key;
    std::string value;
    SplayTree* parent;
    SplayTree* left;
    SplayTree* right;

public:
    SplayTree() : key(NULL), value(NULL), parent(nullptr), left(nullptr), right(nullptr) {}

    SplayTree(const uint64_t& key, const std::string& value) : parent(nullptr), left(nullptr), right(nullptr)
    {
        this->key = key;
        this->value = value;
    }

    ~SplayTree()
    {
        delete this->parent;
        delete this->left;
        delete this->right;
    }

    void add(const uint64_t& new_key, const std::string& new_value)
    {
        return;
    }

    void set(const uint64_t& key, const std::string& new_value)
    {
        return;
    }

    std::string _delete(const uint64_t& key)
    {
        return;
    }

    std::string search(const uint64_t& key)
    {
        return;
    }

    uint64_t min()
    {
        return;
    }

    uint64_t max()
    {
        return;
    }

    void print()
    {
        
    }
};