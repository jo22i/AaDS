#include <iostream>
#include <string>
#include <deque>

class SplayTree
{
    uint64_t key;
    std::string value;
    SplayTree* parent;
    SplayTree* left;
    SplayTree* right;
    bool is_root;

public:
    SplayTree() : key(NULL), value(NULL), parent(nullptr), left(nullptr), right(nullptr), is_root(true) {}

    SplayTree(const uint64_t& key, const std::string& value) : parent(nullptr), left(nullptr), right(nullptr), is_root(true)
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
        if (this->left == nullptr && this->right == nullptr)
        {
            if (this->key == new_key)
            {
                std::cout << "error" << std::endl;
                return;
            }
            else if (this->key > new_key)
            {
                this->left = new SplayTree(new_key, new_value);
                return;
            }
            else
            {
                this->right = new SplayTree(new_key, new_value);
                return;
            }
        }

        std::deque<SplayTree*> stack = {};
        stack.push_front(this->right);
        stack.push_front(this->left);

        while (stack.size() > 0)
        {
            SplayTree* current_elem = stack.front();
            stack.pop_front();

            if (current_elem->key == new_key)
            {
                std::cout << "error" << std::endl;
                return;
            }

            if (current_elem->key > new_key)
            {
                if (current_elem->right == nullptr)
                {
                    current_elem->right = new SplayTree(new_key, new_value);
                    stack.clear();
                    return;
                }
                else
                {
                    stack.push_front(current_elem->right);
                    stack.clear();
                    continue;
                }
            }
            else
            {
                if (current_elem->left == nullptr)
                {
                    current_elem->left = new SplayTree(new_key, new_value);
                    return;
                }
                else
                {
                    stack.push_front(current_elem->left);
                    continue;
                }
            }
        }
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